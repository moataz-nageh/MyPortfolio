/* ============================================================
   Portfolio Website JavaScript
   - Typing animation
   - Smooth scrolling
   - Dark mode toggle (localStorage)
   - Scroll-triggered animations (IntersectionObserver)
   - Navbar state management
   - Mobile menu toggle
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
    initTypingAnimation();
    initSmoothScrolling();
    initDarkMode();
    initNavbarScroll();
    initMobileMenu();
    initActiveNavTracking();
    initCursorGlow();
    initScrollAnimations();
});

/* ───────── Typing Animation ───────── */
function initTypingAnimation() {
    const typingElement = document.getElementById('typing-text');
    if (!typingElement) return;

    const roles = ['AI Engineer', 'Data Analyst'];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    const typeSpeed = 80;
    const deleteSpeed = 50;
    const pauseTime = 2000;

    function type() {
        const currentRole = roles[roleIndex];

        if (isDeleting) {
            typingElement.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
        } else {
            typingElement.textContent = currentRole.substring(0, charIndex + 1);
            charIndex++;
        }

        let delay = isDeleting ? deleteSpeed : typeSpeed;

        if (!isDeleting && charIndex === currentRole.length) {
            delay = pauseTime;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            delay = 400;
        }

        setTimeout(type, delay);
    }

    // Start after a short delay
    setTimeout(type, 800);
}

/* ───────── Smooth Scrolling ───────── */
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                // Close mobile menu if open
                const navMenu = document.getElementById('nav-menu');
                const navToggle = document.getElementById('nav-toggle');
                if (navMenu) navMenu.classList.remove('active');
                if (navToggle) navToggle.classList.remove('active');
                document.body.style.overflow = '';

                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/* ───────── Dark Mode ───────── */
function initDarkMode() {
    const toggle = document.getElementById('dark-mode-toggle');
    const icon = document.getElementById('dark-mode-icon');
    if (!toggle || !icon) return;

    // Check saved preference
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        document.body.classList.add('dark-mode');
        icon.classList.replace('fa-moon', 'fa-sun');
    }

    toggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        const isDark = document.body.classList.contains('dark-mode');

        if (isDark) {
            icon.classList.replace('fa-moon', 'fa-sun');
            localStorage.setItem('theme', 'dark');
        } else {
            icon.classList.replace('fa-sun', 'fa-moon');
            localStorage.setItem('theme', 'light');
        }
    });
}

/* ───────── Scroll Animations (IntersectionObserver) ───────── */
function initScrollAnimations() {
    const fadeElements = document.querySelectorAll('.fade-in');

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                } else {
                    entry.target.classList.remove('visible');
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        fadeElements.forEach(el => observer.observe(el));
    } else {
        // Fallback: show everything
        fadeElements.forEach(el => el.classList.add('visible'));
    }
}

/* ───────── Navbar Scroll Effect ───────── */
function initNavbarScroll() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    }, { passive: true });
}

/* ───────── Mobile Menu ───────── */
function initMobileMenu() {
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    if (!navToggle || !navMenu) return;

    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');

        // Prevent body scroll when menu is open
        if (navMenu.classList.contains('active')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!navMenu.contains(e.target) && !navToggle.contains(e.target)) {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
            document.body.style.overflow = '';
        }
    });
}

/* ───────── Active Nav Link Tracking ───────── */
function initActiveNavTracking() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    if (!sections.length || !navLinks.length) return;

    function determineActiveSection() {
        let currentId = '';
        // Offset triggers activation when a section reaches 30% of viewport height
        const scrollPosition = window.scrollY + (window.innerHeight * 0.3);

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentId = section.getAttribute('id');
            }
        });

        // Corner case: if scrolled to the absolute bottom, select the final section
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 50) {
            currentId = sections[sections.length - 1].getAttribute('id');
        }

        if (currentId) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${currentId}`) {
                    link.classList.add('active');
                }
            });
        }
    }

    window.addEventListener('scroll', determineActiveSection, { passive: true });
    // Initialize state on load
    determineActiveSection();
}

/* ───────── Cursor Glow ───────── */
function initCursorGlow() {
    const cursor = document.getElementById('cursor-glow');
    if (!cursor) return;

    // Disabled on mobile/tablet screens for performance
    if (window.innerWidth <= 992) return;

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let cursorX = window.innerWidth / 2;
    let cursorY = window.innerHeight / 2;
    let isMoving = false;
    let idleTimeout;

    // Track mouse
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        isMoving = true;
        cursor.style.opacity = '1';

        clearTimeout(idleTimeout);
        idleTimeout = setTimeout(() => {
            isMoving = false;
            cursor.style.opacity = '0';
        }, 1500); // fade out after 1.5s idle
    });

    // Hover effect on interactable elements
    const interactables = document.querySelectorAll('a, button, .btn, .nav-link, .social-icon, .card, .skill-card, .timeline-item, .project-card, .service-card, .testimonial-card, .edu-content');
    interactables.forEach(el => {
        el.addEventListener('mouseenter', () => cursor.classList.add('hovered'));
        el.addEventListener('mouseleave', () => cursor.classList.remove('hovered'));
    });

    // Disable effect on mouse leave window
    document.addEventListener('mouseleave', () => {
        cursor.style.opacity = '0';
    });

    // Smooth follow loop (lerp)
    function animate() {
        cursorX += (mouseX - cursorX) * 0.08;
        cursorY += (mouseY - cursorY) * 0.08;

        cursor.style.transform = `translate(${cursorX}px, ${cursorY}px) translate(-50%, -50%)`;

        requestAnimationFrame(animate);
    }
    animate();
}
