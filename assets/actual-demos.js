// Keep all footage silent and only start playback on explicit user interaction.
(()=>{
  for (const card of document.querySelectorAll('.dm-card')) {
    const video=card.querySelector('video');
    const play=card.querySelector('.dm-play');
    if(!video||!play)continue;
    video.muted=true;
    const sync=()=>{card.classList.toggle('dm-playing',!video.paused&&!video.ended)};
    play.addEventListener('click',()=>{
      video.muted=true;
      video.controls=true;
      const result=video.play();
      if(result&&result.catch)result.catch(()=>{card.classList.remove('dm-playing');video.focus()});
    });
    video.addEventListener('play',sync);
    video.addEventListener('pause',sync);
    video.addEventListener('ended',sync);
  }
})();
