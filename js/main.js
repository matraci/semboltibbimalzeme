// -------------------- Dinamik Oluşturma Fonksiyonları --------------------

function renderFeatures() {
    const container = document.getElementById('features-container');
    if (!container) return;
    container.innerHTML = featuresData.map(item => `
        <div class="col-md-4">
            <div class="feature-card scroll-element">
                <div class="feature-icon">
                    <i class="fas ${item.icon}"></i>
                </div>
                <h3>${item.title}</h3>
                <p>${item.description}</p>
            </div>
        </div>
    `).join('');
}

function renderServices() {
    const container = document.getElementById('services-container');
    if (!container) return;
    container.innerHTML = servicesData.map(item => `
        <div class="col-md-4">
            <div class="service-card scroll-element">
                <img src="${item.img}" alt="${item.title}">
                <div class="card-body">
                    <h3>${item.title}</h3>
                    <p>${item.description}</p>
                </div>
            </div>
        </div>
    `).join('');
}

function renderCategories() {
    const container = document.getElementById('categories-container');
    if (!container) return;
    container.innerHTML = categoriesData.map(item => `
        <div class="col-md-3">
            <a href="${item.link}" class="text-decoration-none">
                <div class="category-card scroll-element">
                    <img src="${item.img}" alt="${item.title}">
                    <h4>${item.title}</h4>
                    <p style="color: #666; font-size: 0.85rem; margin-top: 10px;">${item.description}</p>
                </div>
            </a>
        </div>
    `).join('');
}

function renderProducts() {
    const container = document.getElementById('products-container');
    if (!container) return;
    container.innerHTML = productsData.map(item => `
        <div class="col-md-4">
            <a href="${item.link}" class="text-decoration-none">
                <div class="product-card scroll-element">
                    <img src="${item.img}" alt="${item.title}">
                    <div class="card-body">
                        <h4>${item.title}</h4>
                        <p>${item.description}</p>
                        <a href="${item.link}" class="btn btn-sm btn-gradient">Detaylar</a>
                    </div>
                </div>
            </a>
        </div>
    `).join('');
}

// -------------------- Sayfa Yüklendiğinde Çalıştır --------------------

document.addEventListener('DOMContentLoaded', function () {
    renderFeatures();
    renderServices();
    renderCategories();
    renderProducts();

    // Header Scroll
    window.addEventListener('scroll', function () {
        const header = document.getElementById('header');
        if (window.scrollY > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Back to Top
    const backToTop = document.getElementById('backToTop');
    if (backToTop) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 300) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        backToTop.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Scroll Animations
    const scrollElements = document.querySelectorAll('.scroll-element');

    const elementInView = (el, dividend = 1) => {
        const elementTop = el.getBoundingClientRect().top;
        return elementTop <= (window.innerHeight || document.documentElement.clientHeight) / dividend;
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

    const animateCounter = (counter) => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText;
        const inc = target / 50;

        if (count < target) {
            counter.innerText = Math.ceil(count + inc);
            setTimeout(() => animateCounter(counter), 30);
        } else {
            counter.innerText = target + '+';
        }
    };

    const counterSection = document.querySelector('.stats');
    if (counterSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                    entry.target.classList.add('animated');
                    counters.forEach(counter => animateCounter(counter));
                }
            });
        });
        observer.observe(counterSection);
    }

    // Loader
    const loader = document.querySelector('.loader');
    if (loader) {
        setTimeout(() => {
            loader.style.opacity = '0';
            setTimeout(() => {
                loader.style.display = 'none';
            }, 500);
        }, 1500);
    }
});
