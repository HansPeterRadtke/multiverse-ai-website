(() => {
  "use strict";
  const root = document.querySelector(".revision-demo");
  if (!root) return;
  const controls = [...root.querySelectorAll("[data-proof-revision]")];
  const answer = document.getElementById("revision-answer");
  const source = document.getElementById("revision-source-text");
  const sourceLabel = document.getElementById("revision-source-label");
  const validation = document.getElementById("revision-validation");
  const caption = document.getElementById("revision-source-caption");
  fetch("/multiverse-ai-website/assets/kmd/revision-proof.json")
    .then(r => { if (!r.ok) throw new Error("Evidence unavailable"); return r.json(); })
    .then(data => {
      if (!data.cases || data.cases.length !== 2 || data.question !== "Who reviewed the Falcon Test Plan?") {
        throw new Error("Unexpected proof schema");
      }
      function select(id) {
        const value=data.cases.find(x=>x.id===id);
        if(!value) return;
        answer.textContent=value.answer;
        source.textContent=value.evidence_text;
        sourceLabel.textContent=value.rel_path;
        validation.textContent=value.validation;
        caption.textContent=id==="changed"?"Changed original indexed and independently verified":"Original source was indexed and independently verified";
        controls.forEach(b => {
          const active=b.dataset.proofRevision===id;
          b.classList.toggle("active",active);
          b.setAttribute("aria-pressed",String(active));
        });
      }
      controls.forEach(b=>b.addEventListener("click",()=>select(b.dataset.proofRevision)));
      select("original");
    })
    .catch(err => {
      controls.forEach(b=>b.disabled=true);
      caption.textContent="Could not load the recorded source revision evidence.";
      console.warn("KMD recorded proof unavailable:",err.message);
    });
})();
