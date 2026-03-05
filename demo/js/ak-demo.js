/**
 * AK Design System - Demo Logic
 * Centralized logic for demo pages
 */

document.addEventListener('DOMContentLoaded', () => {
    // Update Copyright Year and Company Name
    const year = new Date().getFullYear();
    const companyName = 'ak systems';
    
    // Target elements with specific classes
    document.querySelectorAll('.ak-copyright-year').forEach(el => {
        el.textContent = year >= 2026 ? year : 2026;
    });

    document.querySelectorAll('.ak-company-name').forEach(el => {
        el.textContent = companyName;
    });
    
    // For elements containing the full copyright string (optional helper)
    document.querySelectorAll('[data-ak-copyright]').forEach(el => {
        const currentText = el.textContent;
        // Keep localized "All rights reserved" part if possible
        // This is a simple replacement for the standard pattern
        // "© YYYY Company Name. [Rights]"
        // We replace up to the first dot or end of string
        // This is a bit risky with localization, so specific classes are safer.
    });
});
