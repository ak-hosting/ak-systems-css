/**
 * AK Design System - Demo Logic
 * Centralized logic for demo pages
 */

document.addEventListener('DOMContentLoaded', () => {
    // 0. Initialize Lucide Icons (CDN)
    if (window.lucide) {
        window.lucide.createIcons();
    }

    normalizeDemoSidebar();

    // 1. Update Copyright Year and Company Name (if elements exist)
    const year = new Date().getFullYear();
    const displayYear = year >= 2026 ? year : 2026;
    const companyName = 'ak systems';
    
    document.querySelectorAll('.ak-copyright-year').forEach(el => {
        el.textContent = displayYear;
    });

    document.querySelectorAll('.ak-company-name').forEach(el => {
        el.textContent = companyName;
    });

    // 2. Inject Footer if missing (Centralized Footer Logic)
    // We want to ignore footers inside blockquotes or other components (like the Steve Jobs quote in typography.html)
    const existingFooters = document.querySelectorAll('footer');
    let hasPageFooter = false;
    
    existingFooters.forEach(footer => {
        // If the footer is NOT inside a blockquote, and appears to be a structural footer
        if (!footer.closest('blockquote') && !footer.closest('.ak-card') && !footer.closest('.ak-modal')) {
            hasPageFooter = true;
        }
    });
    
    if (!hasPageFooter) {
        injectFooter(displayYear, companyName);
    }

    const openSidebar = document.getElementById('open-sidebar');
    const closeSidebar = document.getElementById('close-sidebar');
    const sidebarDrawer = document.getElementById('nav-drawer');
    const sidebarLinks = document.querySelectorAll('.ak-sidebar-nav a');

    if (openSidebar && sidebarDrawer) {
        openSidebar.addEventListener('click', () => {
            openModal('nav-drawer');
        });
    }

    if (closeSidebar && sidebarDrawer) {
        closeSidebar.addEventListener('click', () => {
            closeModal('nav-drawer');
        });
    }

    if (sidebarLinks.length > 0 && sidebarDrawer) {
        sidebarLinks.forEach(link => {
            link.addEventListener('click', () => {
                closeModal('nav-drawer');
            });
        });
    }
});

function normalizeDemoSidebar() {
    const sidebarDrawer = document.getElementById('nav-drawer');
    if (!sidebarDrawer) {
        return;
    }

    const lang = document.documentElement.lang || 'en';
    const path = window.location.pathname.split('/').pop() || 'index.html';
    const menuButton = document.querySelector('header .ak-btn.ak-btn-ghost.ak-btn-sm');
    const title = sidebarDrawer.querySelector('.ak-modal-title');
    const body = sidebarDrawer.querySelector('.ak-modal-body');
    const closeButton = document.getElementById('close-sidebar') || sidebarDrawer.querySelector('.ak-modal-header .ak-btn');

    if (menuButton && !menuButton.id) {
        menuButton.id = 'open-sidebar';
        menuButton.setAttribute('type', 'button');
    }

    if (closeButton) {
        closeButton.id = 'close-sidebar';
        closeButton.setAttribute('type', 'button');
    }

    const navText = {
        en: {
            title: 'Documentation',
            close: 'Close',
            overview: 'Overview',
            typography: 'Typography',
            sections: 'Sections',
            colors: 'Colors',
            backgrounds: 'Backgrounds',
            buttons: 'Buttons',
            loaders: 'Loaders',
            forms: 'Forms',
            selectionControls: 'Selection Controls',
            upload: 'Upload',
            cards: 'Cards',
            alerts: 'Alerts',
            modals: 'Modals',
            tables: 'Tables',
            layout: 'Layout',
            extended: 'Extended',
            headers: 'Header & Footer',
            utilities: 'Utility Classes'
        },
        de: {
            title: 'Dokumentation',
            close: 'Schließen',
            overview: 'Übersicht',
            typography: 'Typografie',
            sections: 'Sektionen',
            colors: 'Farben',
            backgrounds: 'Hintergründe',
            buttons: 'Buttons',
            loaders: 'Loaders',
            forms: 'Formulare',
            selectionControls: 'Auswahl',
            upload: 'Upload',
            cards: 'Cards',
            alerts: 'Alerts',
            modals: 'Modals',
            tables: 'Tabellen',
            layout: 'Layout',
            extended: 'Erweitert',
            headers: 'Header & Footer',
            utilities: 'Utilities'
        },
        tr: {
            title: 'Dokümantasyon',
            close: 'Kapat',
            overview: 'Genel Bakış',
            typography: 'Tipografi',
            sections: 'Bölümler',
            colors: 'Renkler',
            backgrounds: 'Arka Planlar',
            buttons: 'Butonlar',
            loaders: 'Yükleyiciler',
            forms: 'Formlar',
            selectionControls: 'Seçim Kontrolleri',
            upload: 'Yükleme',
            cards: 'Kartlar',
            alerts: 'Uyarılar',
            modals: 'Modallar',
            tables: 'Tablolar',
            layout: 'Düzen',
            extended: 'Genişletilmiş',
            headers: 'Header & Footer',
            utilities: 'Utility Classes'
        }
    };

    const localized = navText[lang] || navText.en;
    const prefixes = {
        en: '',
        de: '.de',
        tr: '.tr'
    };
    const suffix = prefixes[lang] || '';
    const indexSuffix = path === 'index.en.html' ? '.en' : suffix;

    const activeGroup = getSidebarGroup(path);
    const items = [
        { key: 'overview', href: `index${indexSuffix}.html` },
        { key: 'typography', href: `typography${suffix}.html` },
        { key: 'sections', href: `sections${suffix}.html` },
        { key: 'colors', href: `index${indexSuffix}.html#colors` },
        { key: 'backgrounds', href: `backgrounds${suffix}.html` },
        { key: 'buttons', href: `buttons${suffix}.html` },
        { key: 'loaders', href: `loaders${suffix}.html` },
        { key: 'layout', href: `layout${suffix}.html` },
        { key: 'forms', href: `forms${suffix}.html` },
        { key: 'selectionControls', href: `selection-controls${suffix}.html` },
        { key: 'upload', href: `upload${suffix}.html` },
        { key: 'cards', href: `cards${suffix}.html` },
        { key: 'alerts', href: `alerts${suffix}.html` },
        { key: 'modals', href: `modals${suffix}.html` },
        { key: 'tables', href: `tables${suffix}.html` },
        { key: 'extended', href: `extended${suffix}.html` },
        { key: 'headers', href: `headers${suffix}.html` },
        { key: 'utilities', href: `index${indexSuffix}.html#utilities` },
    ];

    if (title) {
        title.textContent = localized.title;
    }

    if (closeButton) {
        closeButton.textContent = localized.close;
    }

    if (body) {
        body.innerHTML = `
            <nav aria-label="${localized.title}" class="ak-sidebar-nav ak-text-left">
                <ul class="ak-nav ak-flex-col ak-gap-1 ak-items-start ak-text-left">
                    ${items.map(item => `
                        <li class="ak-w-full">
                            <a href="${item.href}" class="${item.key === activeGroup ? 'ak-active ' : ''}ak-w-full ak-text-left">${localized[item.key]}</a>
                        </li>
                    `).join('')}
                </ul>
            </nav>
        `;
    }
}

function getSidebarGroup(path) {
    if (path.startsWith('typography')) {
        return 'typography';
    }

    if (path.startsWith('sections')) {
        return 'sections';
    }

    if (path.startsWith('backgrounds')) {
        return 'backgrounds';
    }

    if (path.startsWith('buttons')) {
        return 'buttons';
    }

    if (path.startsWith('loaders')) {
        return 'loaders';
    }

    if (path.startsWith('layout')) {
        return 'layout';
    }

    if (path.startsWith('forms')) {
        return 'forms';
    }

    if (path.startsWith('selection-controls')) {
        return 'selectionControls';
    }

    if (path.startsWith('upload')) {
        return 'upload';
    }

    if (path.startsWith('cards')) {
        return 'cards';
    }

    if (path.startsWith('alerts')) {
        return 'alerts';
    }

    if (path.startsWith('modals')) {
        return 'modals';
    }

    if (path.startsWith('tables')) {
        return 'tables';
    }

    if (path.startsWith('extended')) {
        return 'extended';
    }

    if (path.startsWith('headers')) {
        return 'headers';
    }

    if (path.startsWith('index')) {
        return 'overview';
    }

    return 'overview';
}

function injectFooter(year, companyName) {
    const lang = document.documentElement.lang || 'en';
    
    const translations = {
        'en': {
            rights: 'All rights reserved.',
            privacy: 'Privacy Policy',
            terms: 'Terms of Service'
        },
        'de': {
            rights: 'Alle Rechte vorbehalten.',
            privacy: 'Datenschutz',
            terms: 'Nutzungsbedingungen'
        },
        'tr': {
            rights: 'Tüm hakları saklıdır.',
            privacy: 'Gizlilik Politikası',
            terms: 'Kullanım Koşulları'
        }
    };

    const t = translations[lang] || translations['en'];

    const footerHTML = `
    <footer class="ak-footer ak-mt-12 ak-py-8 ak-border-t ak-border-border">
        <div class="ak-container">
            <div class="ak-flex ak-flex-col ak-md:ak-flex-row ak-justify-between ak-items-center">
                <div class="ak-mb-4 ak-md:ak-mb-0">
                    <p class="ak-text-sm ak-text-muted">
                        © <span class="ak-copyright-year">${year}</span> <span class="ak-font-semibold">${companyName}</span>, Inc. ${t.rights}
                    </p>
                </div>
                <div class="ak-flex ak-gap-6">
                    <a href="#" class="ak-text-sm ak-text-muted ak-hover:ak-text-primary">${t.privacy}</a>
                    <a href="#" class="ak-text-sm ak-text-muted ak-hover:ak-text-primary">${t.terms}</a>
                </div>
            </div>
        </div>
    </footer>
    `;

    // Append to body, or after main if main exists
    const main = document.querySelector('main');
    if (main) {
        main.insertAdjacentHTML('afterend', footerHTML);
    } else {
        document.body.insertAdjacentHTML('beforeend', footerHTML);
    }
    
    // Re-initialize Lucide icons if they are used in the footer (none currently, but good practice)
    if (window.lucide) {
        window.lucide.createIcons();
    }
}

// Global Modal Functions
function openModal(id) {
    const modal = document.getElementById(id);
    if (modal) {
        modal.classList.add('ak-modal-open');
        document.body.classList.add('ak-modal-open');
    }
}

function closeModal(id) {
    const modal = document.getElementById(id);
    if (modal) {
        modal.classList.remove('ak-modal-open');
        document.body.classList.remove('ak-modal-open');
    }
}

// Close modal when clicking outside or pressing Escape
document.addEventListener('click', (e) => {
    if (e.target.classList.contains('ak-modal')) {
        e.target.classList.remove('ak-modal-open');
        document.body.classList.remove('ak-modal-open');
    }
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        const openModals = document.querySelectorAll('.ak-modal.ak-modal-open');
        openModals.forEach(modal => {
            modal.classList.remove('ak-modal-open');
        });
        if (openModals.length > 0) {
            document.body.classList.remove('ak-modal-open');
        }
    }
});
