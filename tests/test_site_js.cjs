'use strict';
const fs=require('fs');
const vm=require('vm');
const assert=require('assert');
const script=fs.readFileSync(require('path').join(__dirname,'../assets/site.js'),'utf8');
const state={};
const menu={
  'aria-expanded':'false',
  events:{},
  getAttribute(k){return this[k]},
  setAttribute(k,v){this[k]=v},
  addEventListener(k,fn){this.events[k]=fn}
};
const mobile={open:false,classList:{toggle(k,val){assert.equal(k,'open');mobile.open=val}}};
const form={
 events:{}, valid:true,
 addEventListener(k,fn){this.events[k]=fn},
 reportValidity(){return this.valid}
};
const status={textContent:''};
const data={name:'Taylor Example',email:'taylor@example.com',company:'Acme Lab',problem:'A repeated test workflow needs better handoff and a verified final result.',systems:'Python and local AI'};
const sandbox={
 document:{
  querySelector(selector){return ({'.mobile-toggle':menu,'.mobile-nav':mobile})[selector]||null},
  getElementById(id){return ({'inquiry-form':form,'form-status':status})[id]||null}
 },
 FormData:class {constructor(x){assert.equal(x,form)}get(k){return data[k]||''}},
 window:{location:{href:''}},
 encodeURIComponent
};
vm.runInNewContext(script,sandbox);
assert.equal(typeof form.events.submit,'function');
assert.equal(typeof menu.events.click,'function');
menu.events.click();assert.equal(menu.getAttribute('aria-expanded'),'true');assert.equal(mobile.open,true);
menu.events.click();assert.equal(menu.getAttribute('aria-expanded'),'false');assert.equal(mobile.open,false);
let prevented=false;
form.events.submit({preventDefault(){prevented=true}});
assert.equal(prevented,true);
const uri=sandbox.window.location.href;
assert(uri.startsWith('mailto:multiverse3dhpr@gmail.com?subject='));
const decoded=decodeURIComponent(uri);
assert(decoded.includes('Multiverse technology inquiry — Acme Lab'));
assert(decoded.includes('Current problem and desired result:\nA repeated test workflow'));
assert(decoded.includes('Relevant software or systems: Python and local AI'));
assert(decoded.includes('Reply address: taylor@example.com'));
assert(!decoded.includes('Budget:'));
assert(!decoded.includes('Timeframe:'));
assert(!status.textContent.toLowerCase().includes('was sent'));
form.valid=false;
sandbox.window.location.href='';
form.events.submit({preventDefault(){}});
assert.equal(sandbox.window.location.href,'');
console.log('PASS: menu toggle; local mailto draft fields; no fictitious send; invalid form prevents navigation');
