// SembolTibbi Modern JavaScript

document.addEventListener('DOMContentLoaded', function() {
    
    // Loader
    const loader = document.querySelector('.loader');
    if (loader) {
        setTimeout(() => {
            loader.classList.add('hidden');
        }, 1500);
    }

    // Header Scroll Effect
    const header = document.querySelector('.header-area');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Back to Top Button
    const backToTop = document.querySelector('.back-to-top');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });

    if (backToTop) {
        backToTop.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Scroll Animations
    const scrollElements = document.querySelectorAll('.scroll-element, .fade-in, .slide-in-left, .scale-in');
    
    const elementInView = (el, dividend = 1) => {
        const elementTop = el.getBoundingClientRect().top;
        return (
            elementTop <= 
            (window.innerHeight || document.documentElement.clientHeight) / dividend
        );
    };

    const displayScrollElement = (element) => {
        element.classList.add('scrolled');
    };

    const handleScrollAnimation = () => {
        scrollElements.forEach((el) => {
            if (elementInView(el, 1.25)) {
                displayScrollElement(el);
            }
        });
    };

    window.addEventListener('scroll', handleScrollAnimation);
    handleScrollAnimation();

    // Counter Animation
    const counters = document.querySelectorAll('.stat-number');
    const counterSpeed = 200;

    const animateCounter = (counter) => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText;
        const inc = target / counterSpeed;

        if (count < target) {
            counter.innerText = Math.ceil(count + inc);
            setTimeout(() => animateCounter(counter), 20);
        } else {
            counter.innerText = target;
        }
    };

    // Intersection Observer for Counters
    const counterSection = document.querySelector('.stats-section');
    if (counterSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    counters.forEach(counter => animateCounter(counter));
                    observer.unobserve(entry.target);
                }
            });
        });
        observer.observe(counterSection);
    }

    // Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (hamburger) {
        hamburger.addEventListener('click', function() {
            this.classList.toggle('active');
            mobileMenu.classList.toggle('active');
        });
    }

    // Smooth Scroll for Navigation Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Navbar Active Link on Scroll
    const sections = document.querySelectorAll('section[id]');
    
    window.addEventListener('scroll', () => {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });

        document.querySelectorAll('.main-menu ul li a').forEach(li => {
            li.classList.remove('active');
            if (li.getAttribute('href') === '#' + current) {
                li.classList.add('active');
            }
        });
    });

    // Product Card Hover Effect
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-15px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Feature Cards Stagger Animation
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });

    // Image Lazy Loading
    const images = document.querySelectorAll('img[data-src]');
    const imgOptions = {
        threshold: 0,
        rootMargin: "0px 0px 50px 0px"
    };

    const preloadImage = (img) => {
        const src = img.getAttribute('data-src');
        if (!src) return;
        img.src = src;
        img.removeAttribute('data-src');
    };

    const imgObserver = new IntersectionObserver((entries, imgObserver) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            preloadImage(entry.target);
            imgObserver.unobserve(entry.target);
        });
    }, imgOptions);

    images.forEach(image => {
        imgObserver.observe(image);
    });

    // WhatsApp Float Animation
    const whatsappBtn = document.querySelector('.whatsapp-float');
    if (whatsappBtn) {
        setInterval(() => {
            whatsappBtn.style.transform = 'scale(1.1)';
            setTimeout(() => {
                whatsappBtn.style.transform = 'scale(1)';
            }, 200);
        }, 3000);
    }

    // Form Validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            let isValid = true;
            const inputs = form.querySelectorAll('input[required], textarea[required]');
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('error');
                } else {
                    input.classList.remove('error');
                }
            });

            if (isValid) {
                alert('Mesajınız başarıyla gönderildi!');
                form.reset();
            }
        });
    });

    // Input Focus Effect
    const inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        input.addEventListener('blur', function() {
            if (!this.value) {
                this.parentElement.classList.remove('focused');
            }
        });
    });

    // Parallax Effect for Hero
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', () => {
            const scrolled = window.scrollY;
            heroSection.style.backgroundPositionY = `${scrolled * 0.5}px`;
        });
    }

    // Service Cards Hover 3D Effect
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = (y - centerY) / 20;
            const rotateY = (centerX - x) / 20;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.05, 1.05, 1.05)`;
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
        });
    });

    // Category Cards Click Animation
    const categoryCards = document.querySelectorAll('.category-card');
    categoryCards.forEach(card => {
        card.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });

    // Newsletter Form
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            if (email) {
                alert('Bültenimize abone oldunuz: ' + email);
                this.reset();
            }
        });
    }

    // Loading Progress Bar
    const loadingBar = document.querySelector('.loading-bar');
    if (loadingBar) {
        let width = 0;
        const interval = setInterval(() => {
            if (width >= 100) {
                clearInterval(interval);
            } else {
                width += 5;
                loadingBar.style.width = width + '%';
            }
        }, 30);
    }

    // Tilt Effect for Cards
    const tiltCards = document.querySelectorAll('[data-tilt]');
    tiltCards.forEach(card => {
        card.addEventListener('mousemove', function(e) {
            const x = e.pageX - this.offsetLeft;
            const y = e.pageY - this.offsetTop;
            
            const centerX = this.offsetWidth / 2;
            const centerY = this.offsetHeight / 2;
            
            const rotateX = (y - centerY) / 10;
            const rotateY = (centerX - x) / 10;
            
            this.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'rotateX(0) rotateY(0)';
        });
    });

    // Initialize AOS-like animations
    const initAnimations = () => {
        const animatedElements = document.querySelectorAll('[data-animate]');
        
        animatedElements.forEach(el => {
            const animation = el.getAttribute('data-animate');
            el.classList.add('animate__animated', `animate__${animation}`);
        });
    };

    // Run on load
    initAnimations();
    
    // Re-run on scroll
    window.addEventListener('scroll', initAnimations);

    console.log('SembolTibbi Modern JS Loaded Successfully');
});
