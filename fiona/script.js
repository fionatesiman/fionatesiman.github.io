/**
 * FIONA JUNITA PORTFOLIO — INTERACTIVITY SCRIPT
 * Features:
 * - Responsive Navbar & Scroll Detection
 * - Interactive 16x16 Pixel Drawing Canvas (Based on Zine Slide 8)
 * - Tabbed Zine Exploration
 * - Fullscreen Lightbox Modal
 * - One-click Copy to Clipboard
 */

document.addEventListener('DOMContentLoaded', () => {

  /* ==========================================================================
     1. NAVBAR & MOBILE MENU
     ========================================================================== */
  const navbar = document.getElementById('navbar');
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const navLinks = document.getElementById('nav-links');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });

    // Close mobile nav when clicking a link
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
      });
    });
  }

  /* ==========================================================================
     2. ZINE TABS SWITCHING
     ========================================================================== */
  const tabButtons = document.querySelectorAll('.zine-tab-btn');
  const tabPanels = document.querySelectorAll('.zine-tab-panel');

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-target');
      
      tabButtons.forEach(b => b.classList.remove('active'));
      tabPanels.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const targetPanel = document.getElementById(targetId);
      if (targetPanel) {
        targetPanel.classList.add('active');
      }
    });
  });

  /* ==========================================================================
     3. INTERACTIVE 16x16 PIXEL CANVAS (Slide 8 "Try It Yourself")
     ========================================================================== */
  const canvas = document.getElementById('pixelArtCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    const GRID_SIZE = 16;
    const CANVAS_DIM = 384;
    const PIXEL_SIZE = CANVAS_DIM / GRID_SIZE; // 24px per pixel

    // Initialize 16x16 grid
    let grid = Array(GRID_SIZE).fill(null).map(() => Array(GRID_SIZE).fill('#FFFFFF'));
    let currentColor = '#E51B24';
    let isDrawing = false;
    let isErasing = false;

    const paletteButtons = document.querySelectorAll('.color-btn');
    const activeColorSample = document.getElementById('activeColorSample');
    const activeColorHex = document.getElementById('activeColorHex');
    const eraserBtn = document.getElementById('eraserBtn');
    const clearCanvasBtn = document.getElementById('clearCanvasBtn');
    const downloadPixelBtn = document.getElementById('downloadPixelBtn');
    const presetButtons = document.querySelectorAll('.preset-btn');

    // Palette Selection
    paletteButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        isErasing = false;
        if (eraserBtn) eraserBtn.classList.remove('active');
        paletteButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentColor = btn.getAttribute('data-color');
        if (activeColorSample) activeColorSample.style.backgroundColor = currentColor;
        if (activeColorHex) activeColorHex.textContent = currentColor;
      });
    });

    // Eraser Button
    if (eraserBtn) {
      eraserBtn.addEventListener('click', () => {
        isErasing = !isErasing;
        eraserBtn.classList.toggle('active', isErasing);
        if (isErasing) {
          paletteButtons.forEach(b => b.classList.remove('active'));
          if (activeColorSample) activeColorSample.style.backgroundColor = '#FFFFFF';
          if (activeColorHex) activeColorHex.textContent = 'Eraser';
        } else {
          const defaultBtn = document.querySelector(`.color-btn[data-color="${currentColor}"]`) || paletteButtons[0];
          if (defaultBtn) defaultBtn.classList.add('active');
          if (activeColorSample) activeColorSample.style.backgroundColor = currentColor;
          if (activeColorHex) activeColorHex.textContent = currentColor;
        }
      });
    }

    // Render Function
    function renderGrid() {
      ctx.clearRect(0, 0, CANVAS_DIM, CANVAS_DIM);
      for (let r = 0; r < GRID_SIZE; r++) {
        for (let c = 0; c < GRID_SIZE; c++) {
          ctx.fillStyle = grid[r][c];
          ctx.fillRect(c * PIXEL_SIZE, r * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE);

          // Subtle Grid line
          ctx.strokeStyle = '#F1F5F9';
          ctx.lineWidth = 1;
          ctx.strokeRect(c * PIXEL_SIZE, r * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE);
        }
      }
    }

    // Paint Pixel
    function paintPixel(e) {
      const rect = canvas.getBoundingClientRect();
      const scaleX = canvas.width / rect.width;
      const scaleY = canvas.height / rect.height;
      const clientX = e.clientX || (e.touches && e.touches[0].clientX);
      const clientY = e.clientY || (e.touches && e.touches[0].clientY);

      if (clientX === undefined || clientY === undefined) return;

      const x = (clientX - rect.left) * scaleX;
      const y = (clientY - rect.top) * scaleY;

      const col = Math.floor(x / PIXEL_SIZE);
      const row = Math.floor(y / PIXEL_SIZE);

      if (row >= 0 && row < GRID_SIZE && col >= 0 && col < GRID_SIZE) {
        grid[row][col] = isErasing ? '#FFFFFF' : currentColor;
        renderGrid();
      }
    }

    // Canvas Mouse / Touch Handlers
    canvas.addEventListener('mousedown', (e) => {
      isDrawing = true;
      paintPixel(e);
    });

    window.addEventListener('mouseup', () => {
      isDrawing = false;
    });

    canvas.addEventListener('mousemove', (e) => {
      if (isDrawing) {
        paintPixel(e);
      }
    });

    canvas.addEventListener('touchstart', (e) => {
      isDrawing = true;
      paintPixel(e);
      e.preventDefault();
    }, { passive: false });

    window.addEventListener('touchend', () => {
      isDrawing = false;
    });

    canvas.addEventListener('touchmove', (e) => {
      if (isDrawing) {
        paintPixel(e);
      }
      e.preventDefault();
    }, { passive: false });

    // Clear Canvas
    if (clearCanvasBtn) {
      clearCanvasBtn.addEventListener('click', () => {
        grid = Array(GRID_SIZE).fill(null).map(() => Array(GRID_SIZE).fill('#FFFFFF'));
        renderGrid();
      });
    }

    // Export Canvas as PNG
    if (downloadPixelBtn) {
      downloadPixelBtn.addEventListener('click', () => {
        const link = document.createElement('a');
        link.download = 'fiona_pixels_artwork.png';
        link.href = canvas.toDataURL('image/png');
        link.click();
      });
    }

    // Sprite Presets
    const presets = {
      heart: [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0],
        [0,0,1,2,2,1,0,0,1,2,2,1,0,0,0,0],
        [0,1,2,2,2,2,1,1,2,2,2,2,1,0,0,0],
        [0,1,2,2,2,2,2,2,2,2,2,2,1,0,0,0],
        [0,1,2,2,2,2,2,2,2,2,2,2,1,0,0,0],
        [0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,0],
        [0,0,0,1,2,2,2,2,2,2,1,0,0,0,0,0],
        [0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0],
        [0,0,0,0,0,1,2,2,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      ],
      sword: [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,2,2,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,2,2,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,2,2,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,2,2,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,2,2,0,0,0,0,0,0],
        [0,0,0,0,0,1,1,2,2,0,0,0,0,0,0,0],
        [0,0,0,0,1,3,3,1,0,0,0,0,0,0,0,0],
        [0,0,0,1,3,3,1,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,4,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      ],
      reyna: [
        [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0],
        [0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0],
        [0,0,0,0,1,2,2,2,2,2,2,1,0,0,0,0],
        [0,1,1,1,2,2,2,2,2,2,2,2,1,1,1,0],
        [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
        [0,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0],
        [0,0,1,2,2,2,2,2,2,2,2,2,2,1,0,0],
        [0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0],
        [0,0,1,2,2,2,2,2,2,2,2,2,2,1,0,0],
        [0,1,2,2,2,2,2,1,1,2,2,2,2,2,1,0],
        [1,2,2,2,2,1,1,0,0,1,1,2,2,2,2,1],
        [1,2,2,1,1,0,0,0,0,0,0,1,1,2,2,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      ]
    };

    const presetColorMaps = {
      heart: { 0: '#FFFFFF', 1: '#111827', 2: '#E51B24' },
      sword: { 0: '#FFFFFF', 1: '#111827', 2: '#06B6D4', 3: '#FBBF24', 4: '#E51B24' },
      reyna: { 0: '#FFFFFF', 1: '#111827', 2: '#FBBF24' }
    };

    presetButtons.forEach(pbtn => {
      pbtn.addEventListener('click', () => {
        const type = pbtn.getAttribute('data-preset');
        const pattern = presets[type];
        const cmap = presetColorMaps[type];
        if (pattern && cmap) {
          for (let r = 0; r < GRID_SIZE; r++) {
            for (let c = 0; c < GRID_SIZE; c++) {
              const code = pattern[r][c];
              grid[r][c] = cmap[code] || '#FFFFFF';
            }
          }
          renderGrid();
        }
      });
    });

    // Initial Render
    renderGrid();
  }

  /* ==========================================================================
     4. LIGHTBOX MODAL
     ========================================================================= */
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCaption = document.getElementById('lightboxCaption');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxBackdrop = document.getElementById('lightboxBackdrop');

  const zoomableItems = document.querySelectorAll('.zoomable');

  function openLightbox(src, caption) {
    if (!lightboxModal || !lightboxImg) return;
    lightboxImg.src = src;
    lightboxImg.alt = caption || 'Enlarged Image';
    if (lightboxCaption) lightboxCaption.textContent = caption || '';
    lightboxModal.classList.add('open');
    lightboxModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (!lightboxModal) return;
    lightboxModal.classList.remove('open');
    lightboxModal.setAttribute('aria-hidden', 'true');
    if (lightboxImg) lightboxImg.src = '';
    document.body.style.overflow = '';
  }

  zoomableItems.forEach(item => {
    item.addEventListener('click', (e) => {
      // Don't trigger if clicked on a button or link inside
      if (e.target.closest('button') || e.target.closest('a')) return;

      const imgSrc = item.getAttribute('data-img');
      const caption = item.getAttribute('data-caption');
      if (imgSrc) {
        openLightbox(imgSrc, caption);
      }
    });
  });

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightboxBackdrop) lightboxBackdrop.addEventListener('click', closeLightbox);

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightboxModal && lightboxModal.classList.contains('open')) {
      closeLightbox();
    }
  });

  /* ==========================================================================
     5. ONE-CLICK COPY TO CLIPBOARD
     ========================================================================== */
  const copyButtons = document.querySelectorAll('.copy-btn[data-copy]');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const text = btn.getAttribute('data-copy');
      if (!text) return;

      navigator.clipboard.writeText(text).then(() => {
        const tooltip = btn.querySelector('.tooltip');
        if (tooltip) {
          const original = tooltip.textContent;
          tooltip.textContent = 'Copied!';
          tooltip.style.opacity = '1';
          setTimeout(() => {
            tooltip.textContent = original;
            tooltip.style.opacity = '';
          }, 2000);
        }
      }).catch(err => {
        console.error('Failed to copy to clipboard: ', err);
      });
    });
  });

});
