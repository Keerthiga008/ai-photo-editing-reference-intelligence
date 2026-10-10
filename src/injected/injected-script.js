(() => {
  const eventName = 'ai-photo-editing-reference-click';

  document.addEventListener('click', (event) => {
    const target = event.target;
    if (target instanceof HTMLElement && target.tagName === 'IMG') {
      const payload = {
        type: eventName,
        imageUrl: target.currentSrc || target.src,
        alt: target.alt || 'image'
      };

      window.postMessage(payload, '*');
    }
  });
})();
