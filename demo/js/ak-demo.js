/**
 * AK Design System - Demo Logic
 * Centralized logic for demo pages
 */

document.addEventListener('DOMContentLoaded', () => {
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
    const existingFooter = document.querySelector('footer');
    // We only inject if there is NO footer at all, to avoid duplication on pages that might have custom ones.
    // However, most demo pages (except sections.html) don't have a footer.
    // Let's check if we are on a page that should have a standard footer.
    // We'll append it to the end of .ak-container or body.
    
    if (!existingFooter) {
        injectFooter(displayYear, companyName);
    }
});

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
