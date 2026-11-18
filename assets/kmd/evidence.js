(async () => {
  "use strict";
  const base = "/multiverse-ai-website/assets/kmd/";
  const svg = document.getElementById("evidence-network");
  const inspector = document.getElementById("inspector-content");
  const stats = document.getElementById("graph-stats");
  const cards = document.getElementById("source-cards");
  if (!svg || !inspector || !stats || !cards) return;
  const NS = "http://www.w3.org/2000/svg";
  const make = (tag, attrs = {}, text) => {
    const el = document.createElementNS(NS, tag);
    for (const [key, value] of Object.entries(attrs)) el.setAttribute(key, String(value));
    if (text !== undefined) el.textContent = text;
    return el;
  };
  const plain = (tag, text, cls) => {
    const el = document.createElement(tag);
    if (text !== undefined) el.textContent = text;
    if (cls) el.className = cls;
    return el;
  };
  let data;
  try {
    const response = await fetch(base + "demo-graph.json", { cache: "force-cache" });
    if (!response.ok) throw new Error("HTTP " + response.status);
    data = await response.json();
  } catch (err) {
    inspector.replaceChildren(plain("p", "The verified graph data could not be loaded. " + err.message));
    return;
  }
  const counts = [
    [data.documents.length, "source files"],
    [data.chunks.length, "text chunks"],
    [data.source_spans.length, "source spans"],
    [data.referents.length, "referent candidates"],
    [data.contexts.length, "contexts"],
  ];
  stats.replaceChildren();
  for (const [count, label] of counts) {
    const el = plain("span");
    el.append(plain("strong", String(count)), document.createTextNode(label));
    stats.append(el);
  }
  const by = (items, key) => new Map(items.map((item) => [item[key], item]));
  const docMap = by(data.documents, "document_id");
  const chunkMap = by(data.chunks, "chunk_id");
  const spanMap = by(data.source_spans, "span_id");
  const mentionMap = by(data.mentions, "mention_id");
  const nodes = [];
  const N = (id, type, data, x, y, label, short) => nodes.push({id, type, data, x, y, label: String(label ?? "Unspecified context"), short});
  data.documents.forEach((d, i) => N("d:" + d.document_id, "doc", d, 140, 145 + i * 165, d.rel_path.split("/").at(-1), "FILE " + (i+1)));
  data.chunks.forEach((c, i) => N("c:" + c.chunk_id, "chunk", c, 405, 63 + i * 53.5, "Chunk " + (i + 1), "C" + String(i + 1).padStart(2, "0")));
  data.referents.forEach((r, i) => N("r:" + r.referent_id, "ref", r, 755, 50 + i * 52, r.canonical_label, "R" + String(i + 1).padStart(2, "0")));
  data.contexts.forEach((ctx, i) => N("x:" + ctx.context_id, "ctx", ctx, 1060, 145 + i * 170, ctx.holder_surface, "CTX" + (i + 1)));
  const nodeMap = by(nodes,"id");
  const edges = [];
  const edgeKeys = new Set();
  const E = (a,b,type) => {
    if (!nodeMap.has(a) || !nodeMap.has(b)) return;
    const key = a + "/" + b + "/" + type;
    if (!edgeKeys.has(key)) { edgeKeys.add(key); edges.push({a,b,type}); }
  };
  data.chunks.forEach((c) => E("d:" + c.document_id, "c:" + c.chunk_id, "sources"));
  for (const link of data.mention_referents) {
    const mention = mentionMap.get(link.mention_id);
    const span = mention && spanMap.get(mention.span_id);
    if (span) E("c:" + span.chunk_id, "r:" + link.referent_id, "entities");
  }
  for (const link of data.context_assignments) {
    if (link.applies_to_type === "chunk") E("c:" + link.applies_to_id, "x:" + link.context_id, "contexts");
  }
  const edgeLayer = make("g",{"aria-hidden":"true"});
  const nodeLayer = make("g");
  svg.append(edgeLayer,nodeLayer);
  const edgeVisual = [];
  for (const edge of edges) {
    const a = nodeMap.get(edge.a),b = nodeMap.get(edge.b);
    const dx = (b.x-a.x)*0.51;
    const path = make("path", {d:`M ${a.x} ${a.y} C ${a.x+dx} ${a.y}, ${b.x-dx} ${b.y}, ${b.x} ${b.y}`,class:"edge edge-"+edge.type});
    edgeLayer.append(path);
    edgeVisual.push({...edge,el:path});
  }
  const nodeVisual = [];
  for (const node of nodes) {
    const group = make("g",{class:"node "+node.type,tabindex:"0",role:"button","aria-label":node.type + ": " + node.label});
    const radius = node.type === "doc" ? 28 : node.type === "ctx" ? 23 : node.type === "ref" ? 17 : 13;
    group.append(make("circle",{cx:node.x,cy:node.y,r:radius,strokeWidth:1.7}));
    const tag = make("text",{x:node.x,y:node.y+4,"text-anchor":"middle","font-size":10},node.short);
    group.append(tag);
    if(node.type === "doc" || node.type === "ctx" || node.type === "ref") {
      const t = make("text",{x:node.x,y:node.y+radius+19,"text-anchor":"middle","font-size":10},node.label.length>24?node.label.slice(0,21)+"…":node.label);
      group.append(t);
    }
    group.addEventListener("click",()=>select(node.id));
    group.addEventListener("keydown",(e)=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();select(node.id);}});
    const hint = make("title",{},node.type + ": " + node.label);group.append(hint);
    nodeLayer.append(group); nodeVisual.push({...node,el:group});
  }
  let current = null;
  let mode="all";
  const field = (key,val) => {
    const dt=plain("dt",key),dd=plain("dd",val===undefined?"unknown":String(val));
    return [dt,dd];
  };
  const fillInspector = (node) => {
    inspector.replaceChildren();
    const category = {
      doc:"Original source file",
      chunk:"Original text chunk",
      ref:"Candidate referent",
      ctx:"Discourse / quality context"
    }[node.type];
    inspector.append(plain("h3",node.label),plain("p",category));
    const dl=plain("dl");
    if(node.type==="doc"){
      dl.append(...field("RELATIVE PATH",node.data.rel_path),...field("FILE BYTES",node.data.size_bytes),...field("SHA-256 VERIFIED",node.data.content_validated_sha256?"Yes":"No"));
      inspector.append(dl,plain("pre",node.data.content));
    }else if(node.type==="chunk"){
      const doc=docMap.get(node.data.document_id);
      dl.append(...field("SOURCE",doc?.rel_path||"unknown"),...field("CHARACTER RANGE",node.data.char_start+"–"+node.data.char_end),...field("CHUNK ORDER",node.data.chunk_order),...field("SOURCE SPANS",data.source_spans.filter((s)=>s.chunk_id===node.data.chunk_id).length));
      inspector.append(dl,plain("pre",node.data.text));
    }else if(node.type==="ref"){
      const links=data.mention_referents.filter((m)=>m.referent_id===node.data.referent_id);
      dl.append(...field("ENTITY LABEL",node.data.canonical_label),...field("STATUS",node.data.status),...field("MENTION LINKS",links.length));
      inspector.append(dl);
      const text=links.map((link)=>{const m=mentionMap.get(link.mention_id);const s=m&&spanMap.get(m.span_id);const d=s&&docMap.get(s.document_id);return (m?.surface||"unknown")+" — "+(d?.rel_path||"unknown");}).slice(0,7).join("\n");
      inspector.append(plain("pre",text||"No linked mentions"));
    }else{
      dl.append(...field("CONTEXT KIND",node.data.kind),...field("SOURCE CARRIER",node.data.holder_surface),...field("LINKED CHUNKS",data.context_assignments.filter((c)=>c.context_id===node.data.context_id&&c.applies_to_type==="chunk").length));
      inspector.append(dl,plain("p","This is an indexed context label, not a proof that the underlying claim is true."));
    }
  };
  function select(id){
    current=id;
    const node=nodeMap.get(id);
    if(!node)return;
    fillInspector(node);
    redraw();
  }
  function redraw(){
    const neighborhood=new Set(current?[current]:[]);
    if(current)for(const edge of edges){if(edge.a===current)neighborhood.add(edge.b);if(edge.b===current)neighborhood.add(edge.a);}
    for(const edge of edgeVisual){
      const present=(mode==="all"||edge.type===mode);
      const highlighted=current&&(edge.a===current||edge.b===current);
      edge.el.style.display=present?"":"none";
      edge.el.style.opacity=!present?0:current?(highlighted?".96":".10"):".38";
      edge.el.classList.toggle("active",!!highlighted);
    }
    for(const node of nodeVisual){
      const present=mode==="all"||node.type==="doc"||node.type==="chunk"||(mode==="entities"&&node.type==="ref")||(mode==="contexts"&&node.type==="ctx");
      node.el.style.display=present?"":"none";
      node.el.classList.toggle("selected",node.id===current);
      node.el.classList.toggle("dim",!!current&&!neighborhood.has(node.id));
    }
  }
  document.querySelectorAll("#network-filters button").forEach(button=>{
    button.addEventListener("click",()=>{
      mode=button.dataset.mode;
      document.querySelectorAll("#network-filters button").forEach(b=>{const on=b===button;b.classList.toggle("active",on);b.setAttribute("aria-pressed",String(on));});
      redraw();
    });
  });
  cards.replaceChildren();
  for (const documentRecord of data.documents) {
    const article=plain("article",undefined,"source-card");
    const top=plain("div",undefined,"source-card-top");
    top.append(plain("span","ORIGINAL SOURCE FILE"),plain("strong",documentRecord.rel_path));
    const body=plain("div",documentRecord.content,"source-card-body");
    const foot=plain("div",(documentRecord.content_validated_sha256?"SHA-256 VERIFIED · ":"UNVERIFIED · ")+documentRecord.size_bytes+" BYTES","source-card-foot");
    article.append(top,body,foot);
    cards.append(article);
  }
  select("d:"+data.documents[0].document_id);
})();
