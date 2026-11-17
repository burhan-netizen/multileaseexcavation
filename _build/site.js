(function(){
  var d=document, root=d.documentElement;
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* mobile menu */
  var hdr=d.querySelector('.header'), mb=d.querySelector('.menu-btn');
  if(mb){
    mb.addEventListener('click',function(){
      var open=hdr.classList.toggle('menu-open');
      mb.setAttribute('aria-expanded',open?'true':'false');
    });
    d.querySelectorAll('.nav-links a').forEach(function(a){a.addEventListener('click',function(){hdr.classList.remove('menu-open');mb.setAttribute('aria-expanded','false');});});
    d.addEventListener('keydown',function(e){if(e.key==='Escape'&&hdr.classList.contains('menu-open')){hdr.classList.remove('menu-open');mb.setAttribute('aria-expanded','false');mb.focus();}});
  }

  /* hero headline */
  var h1=d.querySelector('.hero h1');
  if(h1){requestAnimationFrame(function(){requestAnimationFrame(function(){h1.classList.add('go');});});}

  /* reveal on scroll */
  var rev=[].slice.call(d.querySelectorAll('[data-reveal]'));
  if('IntersectionObserver' in window && !reduce){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px'});
    rev.forEach(function(el,i){el.style.transitionDelay=(el.dataset.delay||0)+'ms';io.observe(el);});
    setTimeout(function(){rev.forEach(function(el){el.classList.add('in');});},6000);
  } else rev.forEach(function(el){el.classList.add('in');});

  /* lazy videos: load when near, play only in view */
  var vids=[].slice.call(d.querySelectorAll('video[data-src]'));
  function load(v){if(!v.src){v.src=v.dataset.src;}}
  if('IntersectionObserver' in window){
    var vo=new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;
      if(e.isIntersecting){load(v); if(!reduce){var p=v.play(); if(p&&p.catch)p.catch(function(){});}}
      else if(!v.paused){v.pause();}
    });},{rootMargin:'200px 0px'});
    vids.forEach(function(v){vo.observe(v);});
  }

  /* hero video starts after page load so the poster is the LCP */
  window.addEventListener('load',function(){
    var hv=d.querySelector('.hero video[data-src]'); if(hv){load(hv); if(!reduce){var p=hv.play(); if(p&&p.catch)p.catch(function(){});}}
  });

  /* pinned story (desktop only, motion allowed) */
  var story=d.querySelector('.story');
  if(story && !reduce && window.matchMedia('(min-width: 1000px) and (min-height: 640px)').matches){
    story.classList.add('pin');
    var steps=[].slice.call(story.querySelectorAll('.step'));
    var layers=[].slice.call(story.querySelectorAll('.story-stage .layer'));
    var scroller=story.querySelector('.story-scroller');
    var fill=story.querySelector('.rail .fill'), dig=story.querySelector('.rail .dig'), rail=story.querySelector('.rail');
    story.style.setProperty('--steps',steps.length);
    var cur=-1, ticking=false;
    function setStep(i){
      if(i===cur)return; cur=i;
      steps.forEach(function(s,k){s.classList.toggle('on',k===i); s.setAttribute('aria-hidden',k===i?'false':'true');});
      layers.forEach(function(l,k){l.classList.toggle('on',k===i); var v=l.querySelector('video'); if(v){ if(k===i){load(v); var p=v.play(); if(p&&p.catch)p.catch(function(){});} else v.pause(); }});
    }
    function upd(){
      ticking=false;
      var r=scroller.getBoundingClientRect(), vh=window.innerHeight;
      var p=Math.min(1,Math.max(0,-r.top/(r.height-vh)));
      setStep(Math.min(steps.length-1,Math.floor(p*steps.length*0.999)));
      if(fill) fill.style.transform='scaleX('+p+')';
      if(dig&&rail) dig.style.transform='translateX('+(p*(rail.clientWidth-54))+'px)';
    }
    window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(upd);}},{passive:true});
    window.addEventListener('resize',upd);
    upd();
  }

  /* fleet gate check */
  var range=d.getElementById('gate');
  if(range){
    var out=d.getElementById('gate-out'), verdict=d.getElementById('gate-verdict');
    var machs=[].slice.call(d.querySelectorAll('.mach'));
    function gate(){
      var w=parseFloat(range.value); out.textContent=w.toFixed(1)+' m';
      var fits=[];
      machs.forEach(function(m){var need=parseFloat(m.dataset.needs); var ok=w>=need;
        m.classList.toggle('no',!ok); m.querySelector('.fit').textContent=ok?'Fits':'Too wide'; if(ok)fits.push(m.dataset.name);});
      if(!fits.length) verdict.textContent='Under a metre? Ask us about a micro excavator from about 0.7 m. Send a photo of the access and we will tell you straight.';
      else if(fits.length===machs.length) verdict.textContent='Plenty of room. The whole fleet can get in, including tippers for same day cart away.';
      else verdict.textContent='At '+w.toFixed(1)+' m we can bring in: '+fits.join(', ')+'.';
    }
    range.addEventListener('input',gate); gate();
  }

  /* project rail buttons */
  d.querySelectorAll('[data-rail]').forEach(function(b){
    b.addEventListener('click',function(){var r=d.getElementById(b.dataset.rail); var c=r.querySelector('.prj'); var step=c?c.getBoundingClientRect().width+16:320;
      r.scrollBy({left:(b.dataset.dir==='prev'?-1:1)*step,behavior:reduce?'auto':'smooth'});});
  });

  /* depth gauge + footer parallax + mobile bar */
  var gauge=d.querySelector('.gauge'), lvl=gauge&&gauge.querySelector('.lvl'), val=gauge&&gauge.querySelector('.val');
  var mbar=d.querySelector('.mbar'), darks=[].slice.call(d.querySelectorAll('.hero,.band,.page-hero'));
  var maxDepth=parseFloat(gauge?gauge.dataset.max:6)||6, t2=false;
  function onScroll(){
    t2=false;
    var y=window.scrollY, h=d.documentElement.scrollHeight-window.innerHeight, p=h>0?Math.min(1,y/h):0;
    if(gauge){lvl.style.transform='scaleY('+p+')'; val.textContent='Depth '+(p*maxDepth).toFixed(1)+' m';
      var mid=window.innerHeight/2, dark=darks.some(function(s){var r=s.getBoundingClientRect();return r.top<mid&&r.bottom>mid;});
      gauge.classList.toggle('on-dark',dark);}
    if(mbar) mbar.classList.toggle('show',y>window.innerHeight*0.6);
  }
  window.addEventListener('scroll',function(){if(!t2){t2=true;requestAnimationFrame(onScroll);}},{passive:true});
  onScroll();

  /* demo form */
  d.querySelectorAll('form.quote').forEach(function(f){
    f.addEventListener('submit',function(e){e.preventDefault();
      if(!f.checkValidity()){f.reportValidity();return;}
      f.classList.add('sent'); var ok=f.querySelector('.ok'); ok.focus();
    });
  });
})();
