#!/usr/bin/env python3
"""Reposition real Blender assets as proof of multi-host autonomous AI production.

Preserve original model-catalog links, real media and photo provenance. Only
verified real Blender renders are used; do not imply photorealism acceptance.
"""
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
import hashlib,json
R=Path(__file__).resolve().parents[1]
base='/multiverse-ai-website/'
source={
 'warehouse-exterior': '/data/var/3d-quality-20261028/photographic_rebuild/warehouse_genuine_exterior_three_docks_ground_camera_v2.png',
 'warehouse-forklift': '/data/var/3d-quality-20261031/warehouse_v94_fullhd_genuine/WAREHOUSE_V94_REAL_GROUNDED_FORKLIFT_AND_WORKING_RACKS_1920.png',
 'loading-dock': '/data/var/3d-quality-20261028/photographic_rebuild/dock_v7_actual_light_canopy_and_raised_loading_bay.png',
}
output=R/'assets/3d/agent-made';output.mkdir(parents=True,exist_ok=True)
receipts=[]
for name,original in source.items():
 p=Path(original);assert p.is_file(),('missing authenticated Blender render',p)
 data=p.read_bytes();im=Image.open(p).convert('RGB');ow,oh=im.size
 if im.width>1920:im.thumbnail((1920,1080),Image.Resampling.LANCZOS)
 out=output/(name+'.webp')
 im.save(out,'WEBP',quality=84,method=6)
 Image.open(out).verify()
 receipts.append({'image':str(out.relative_to(R)),'source_asset_name':p.name,'source_sha256':hashlib.sha256(data).hexdigest(),'source_dims':[ow,oh],'result_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'result_bytes':out.stat().st_size,'provenance':'actual Blender Cycles scene render','quality_boundary':'visual candidate; photographic realism not owner-certified'})
(output/'source-receipts.json').write_text(json.dumps(receipts,indent=2)+'\n')
# Keep full machine-local source paths in private QA records only, never in
# the public GitHub Pages asset directory.
private=Path('/data/var/multiverse-kmd/3d-agent-production-source-paths-20261120.json')
private.write_text(json.dumps({'source_paths':source,'outputs':receipts},indent=2)+'\n')
print('REAL RENDERS',[(r['image'],r['result_bytes']) for r in receipts])

def newsection(html):return BeautifulSoup(html,'html.parser').select_one('section')

def addstyle(s):
    href=base+'assets/3d-agent-production.css'
    if not s.select_one('head link[href="'+href+'"]'):
        s.head.append(s.new_tag('link',rel='stylesheet',href=href))

def render_3d():
 p=R/'3d/index.html';s=BeautifulSoup(p.read_text(),'html.parser')
 m=s.select_one('main#main');assert m
 # Idempotency: remove only previously generated marketing sections, leave
 # original published catalog and other pages untouched on every rebuild.
 for old in m.select('section.ap-process,section.ap-work,section.ap-capability,section.ap-machines,section.ap-motion'):
     old.decompose()
 hero=m.select_one('section#top');assert hero
 hero.replace_with(newsection('''<section class="ap-hero" id="top"><div class="container ap-hero-inner"><div class="ap-hero-copy"><p class="ap-kicker">MULTIVERSE · AI-OPERATED 3D PRODUCTION</p><h1>This 3D scene was built through <em>AI-directed Blender workflows.</em></h1><p class="ap-lead">The impressive part is not another downloadable model. It is the production system behind it: AI agents write and run Blender/Python tools, iterate on geometry and materials, create animation and renders, and check export files across my own network of machines.</p><div class="ap-hero-buttons"><a class="ap-button ap-primary" href="#pipeline">See how the agents produce it</a><a class="ap-button ap-secondary" href="#visual-proof">View actual Blender renders</a></div><p class="ap-understatement">Genuine scene render · Independently built pipeline · Human quality review remains part of production</p></div><div class="ap-hero-art"><img src="/multiverse-ai-website/assets/3d/agent-made/warehouse-exterior.webp" width="1600" height="900" alt="Genuine Blender Cycles render of an industrial warehouse exterior with three modeled loading docks" fetchpriority="high"/><span>REAL BLENDER SCENE RENDER · NOT A GENERATED STOCK PHOTO</span></div></div></section>'''))
 old=s.select_one('#pipeline');
 if old:old.decompose()
 first=m.select_one('section#catalog');assert first
 first.insert_before(newsection('''<section class="ap-process" id="pipeline"><div class="container"><p class="ap-kicker">THE TECHNOLOGY BEHIND THE IMAGES</p><h2>I built the pipeline. <em>AI agents run the tools.</em></h2><p class="ap-intro">This is a custom production workflow using my own machines and software—not an account on a one-click 3D generation service. ChatGPT-assisted and locally hosted AI agents can coordinate development and review tasks while Blender and Python perform the concrete engineering work.</p><div class="ap-process-grid"><article><span>01 / PLAN &amp; DIRECT</span><h3>Translate a product goal into jobs.</h3><p>Agents work from asset requirements, study industrial references, propose geometry, materials, cameras and mechanical motion, and prepare scripts or tasks for the next step.</p></article><article><span>02 / BUILD IN BLENDER</span><h3>Create editable geometry and animation.</h3><p>Blender/Python constructs machinery, racks, industrial rooms and moving parts. Material pipelines build PBR maps and scene lighting; native .blend projects remain editable.</p></article><article><span>03 / RENDER &amp; INSPECT</span><h3>Test the work across machines.</h3><p>Rendering and verification operate on available systems. Image and video analysis, source inspection, collision and geometry checks help identify problems before a new revision.</p></article><article><span>04 / EXPORT &amp; VALIDATE</span><h3>Package real usable model files.</h3><p>Automated checks exercise GLB/glTF and other supported formats, clean reimports, animation and scene integrity. Marketplace packaging is a distinct final step, not proof of photorealism.</p></article></div><p class="ap-proof-note">The agents automate substantial authoring and evaluation work. That does not imply every decision is made without human input, that every scene is photorealistic, or that every export already meets all engine and marketplace requirements.</p></div></section>'''))
 first.insert_before(newsection('''<section class="ap-work" id="visual-proof"><div class="container"><p class="ap-kicker">ACTUAL WORK · ACTUAL BLENDER RENDERS</p><h2>The output is visible. <em>The engineering is inspectable.</em></h2><p class="ap-intro">These images come from real editable Blender scenes used during the industrial warehouse and loading-dock development. They are not AI-generated concept illustrations or unrelated reference photographs. Different revisions have different levels of visual approval.</p><div class="ap-showcase"><figure class="ap-main-shot"><img src="/multiverse-ai-website/assets/3d/agent-made/warehouse-exterior.webp" width="1600" height="900" loading="lazy" alt="Rendered three-bay industrial warehouse with authored cladding, bay doors, levelers and paved yard"/><figcaption><strong>Industrial warehouse — full exterior</strong><span>Real Cycles render; approved October production presentation scene, still subject to further realism work</span></figcaption></figure><figure><img src="/multiverse-ai-website/assets/3d/agent-made/warehouse-forklift.webp" width="1920" height="1080" loading="lazy" alt="Genuine Blender-rendered forklift with industrial racking, pallets and warehouse lighting"/><figcaption><strong>Forklift and warehouse logistics</strong><span>Development scene with modeled forklift, loads and rack structures; not a certified photographic match</span></figcaption></figure><figure><img src="/multiverse-ai-website/assets/3d/agent-made/loading-dock.webp" width="1600" height="900" loading="lazy" alt="Genuine Blender render of a warehouse loading dock with modeled canopy, door, lip and leveler details"/><figcaption><strong>Loading dock and mechanical detail</strong><span>Editable PBR scene render with industrial staging; photographic realism remains under review</span></figcaption></figure></div></div></section>'''))
 first.insert_before(newsection('''<section class="ap-capability"><div class="container ap-capability-grid"><div><p class="ap-kicker">WHY THIS MATTERS BEYOND 3D MODELS</p><h2>AI doing production work—not just producing suggestions.</h2><p>The same engineering method applies to other defined software tasks: an agent receives an objective, uses real applications through tools, produces artifacts, runs repeatable checks and records what passed or failed. The 3D pipeline is a tangible demonstration of that capability, with visible products rather than an abstract agent diagram.</p></div><div class="ap-capability-points"><p><strong>Owned infrastructure.</strong> Blender, Python, models and validation tools operate on local machines under direct control.</p><p><strong>Multi-step execution.</strong> Geometry, texturing, animation, rendering, testing and packaging are connected workflows.</p><p><strong>Reproducible evidence.</strong> Scenes, scripts, source renders and validation receipts enable technical inspection instead of relying on screenshots alone.</p><p><strong>Honest quality gates.</strong> Commercial acceptability and photographic realism are separate assessments; visual defects remain open where not yet resolved.</p></div></div></section>'''))
 first.insert_before(newsection('''<section class="ap-machines"><div class="container"><p class="ap-kicker">CUSTOM MULTI-MACHINE SETUP</p><h2>Different tools, different machines. One production workflow.</h2><div class="ap-machine-grid"><div><strong>Nitro · Blender and Python</strong><p>Builds geometry, materials, exports and independent visual and file checks from reproducible project scripts.</p></div><div><strong>Thor · Heavy AI and rendering</strong><p>Runs larger local models and supports demanding rendering or visual-computation work where capacity allows.</p></div><div><strong>Jetson · Visual analysis</strong><p>Local vision-model experiments inspect animation contact sheets and report findings about candidate outputs.</p></div><div><strong>Raspi · Shared coordination</strong><p>Provides infrastructure documentation, project exchange and resource-broker controls so different workers do not blindly compete for hardware.</p></div></div><p class="ap-machine-caveat">Agent tools and human-reviewed ChatGPT workflows coordinate parts of this production. These are documented system roles, not a claim that a single unified job automatically runs every stage on every host.</p></div></section>'''))
 first.insert_before(newsection('''<section class="ap-motion" id="motion-proof"><div class="container"><p class="ap-kicker">REAL MOTION · REAL DELIVERABLES</p><h2>Editable assets are only the start. The machinery moves.</h2><p class="ap-intro">Original project animation previews from the Blender-based industrial production pipeline. Play the recorded clips and inspect the separate marketplace packages below for the exact supported animation and export formats.</p><div class="ap-motion-grid"><figure><video controls muted preload="none" playsinline poster="/multiverse-ai-website/assets/demos/animated-forklift-poster.webp"><source src="/multiverse-ai-website/assets/demos/animated-forklift.mp4" type="video/mp4"/>Your browser does not support embedded video.</video><figcaption><strong>Animated forklift</strong><span>Wheel, steering and lift animation preview · real model footage</span></figcaption></figure><figure><video controls muted preload="none" playsinline poster="/multiverse-ai-website/assets/demos/warehouse-loading-dock-poster.webp"><source src="/multiverse-ai-website/assets/demos/warehouse-loading-dock.mp4" type="video/mp4"/>Your browser does not support embedded video.</video><figcaption><strong>Mechanical loading dock</strong><span>Animated original loading-bay model · actual project video</span></figcaption></figure></div></div></section>'''))
 first.select_one('.pf-section-top h2').string='Models produced through this system.'
 first.select_one('.pf-section-top > p:last-child').string='The following individual downloadable products are examples of output. See each marketplace listing for its exact included files and licensing.'
 oldheading=first.select_one('.pf-section-top .pf-eyebrow')
 if oldheading:oldheading.string='SECONDARY / 3D MODEL CATALOG'
 # Keep all existing media and marketplace links, only shift their priority.
 s.title.string='AI-Directed 3D Production with Blender | Multiverse'
 description=s.find('meta',attrs={'name':'description'})
 if description:description['content']='See how AI agents operate a custom multi-machine Blender/Python pipeline to create industrial 3D geometry, animation, genuine Cycles renders and validated model exports.'
 addstyle(s);p.write_text(str(s).rstrip()+'\n')
 print('POSITIONED /3d/: agent workflow + original Blender renders + secondary catalog')

def render_home():
 p=R/'index.html';s=BeautifulSoup(p.read_text(),'html.parser')
 old=s.select_one('#industrial-assets');assert old
 old.replace_with(newsection('''<section class="ap-home-feature" id="industrial-assets"><div class="container ap-home-layout"><div class="ap-home-media"><img src="/multiverse-ai-website/assets/3d/agent-made/warehouse-exterior.webp" width="1600" height="900" loading="lazy" alt="Actual Blender industrial warehouse exterior created through agent-directed production scripts"/><span>ORIGINAL BLENDER SCENE · AI-DIRECTED PRODUCTION</span></div><div class="ap-home-copy"><p class="ap-kicker">A VISIBLE EXAMPLE OF AI WORKING</p><h2>AI agents built this industrial 3D scene.</h2><p>The technology is the story. I built a multi-machine production setup where AI agents use Blender and Python to create geometry, animate machinery, render real scenes and validate finished files. These are actual model outputs, not generated concept art.</p><p class="ap-home-caveat">Realism is still being improved; some published and private development scenes remain below the target photographic standard.</p><a class="ap-button ap-primary" href="/multiverse-ai-website/3d/">See the AI production system</a></div></div></section>'''))
 # The production capability is evidence of the agent platform. Feature it
 # after the two main software systems, not buried beneath unrelated products.
 feature=s.select_one('#industrial-assets');wix=s.select_one('#software-proof')
 assert feature and wix
 feature.extract();wix.insert_before(feature)
 addstyle(s);p.write_text(str(s).rstrip()+'\n')
 print('POSITIONED HOME 3D: autonomous work evidence rather than model shop')

render_3d();render_home()
