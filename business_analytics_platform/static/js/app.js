/**
 * Main Application Orchestrator, SPA Router, Theme Manager & Global Event Bus
 */
const App = {
    currentRoute: 'overview',
    activeDataset: '',
    datasetsList: [],

    async init() {
        this.initTheme();
        this.initNavigation();
        this.initMobileDrawer();
        await this.refreshDatasetSelector();
        this.navigateTo(this.getHashRoute() || 'overview');

        // Listen to hash changes for deep linking
        window.addEventListener('hashchange', () => {
            this.navigateTo(this.getHashRoute() || 'overview');
        });
    },

    getHashRoute() {
        const hash = window.location.hash.replace('#', '');
        return ['overview', 'datamanager', 'sales', 'products', 'profit', 'ai-insights', 'reports'].includes(hash) ? hash : 'overview';
    },

    initTheme() {
        const savedTheme = localStorage.getItem('theme') || 'dark';
        if (savedTheme === 'dark') {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
        this.updateThemeToggleIcon();

        const themeBtn = document.getElementById('theme-toggle-btn');
        if (themeBtn) {
            themeBtn.addEventListener('click', () => {
                const isDark = document.documentElement.classList.toggle('dark');
                localStorage.setItem('theme', isDark ? 'dark' : 'light');
                this.updateThemeToggleIcon();
                // Refresh active charts with new theme colors
                ChartManager.updateAllThemes();
            });
        }
    },

    updateThemeToggleIcon() {
        const isDark = document.documentElement.classList.contains('dark');
        const sunIcon = document.getElementById('theme-sun-icon');
        const moonIcon = document.getElementById('theme-moon-icon');
        if (sunIcon && moonIcon) {
            if (isDark) {
                sunIcon.classList.remove('hidden');
                moonIcon.classList.add('hidden');
            } else {
                sunIcon.classList.add('hidden');
                moonIcon.classList.remove('hidden');
            }
        }
        if (window.lucide) window.lucide.createIcons();
    },

    initNavigation() {
        const navLinks = document.querySelectorAll('[data-route]');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const route = link.getAttribute('data-route');
                window.location.hash = '#' + route;
                this.closeMobileDrawer();
            });
        });
    },

    initMobileDrawer() {
        const toggleBtn = document.getElementById('mobile-drawer-toggle');
        const closeBtn = document.getElementById('mobile-drawer-close');
        const sidebar = document.getElementById('main-sidebar');

        if (toggleBtn && sidebar) {
            toggleBtn.addEventListener('click', () => {
                sidebar.classList.toggle('-translate-x-full');
            });
        }

        if (closeBtn && sidebar) {
            closeBtn.addEventListener('click', () => {
                this.closeMobileDrawer();
            });
        }
    },

    closeMobileDrawer() {
        const sidebar = document.getElementById('main-sidebar');
        if (sidebar && window.innerWidth < 1024) {
            sidebar.classList.add('-translate-x-full');
        }
    },

    async refreshDatasetSelector() {
        try {
            const res = await fetch('/api/datasets');
            const data = await res.json();
            if (data.status === 'success') {
                this.datasetsList = data.datasets;
                this.activeDataset = data.active;
                this.renderDatasetDropdown(data.datasets, data.active);
            }
        } catch (err) {
            console.error('Error fetching datasets:', err);
        }
    },

    renderDatasetDropdown(datasets, active) {
        const select = document.getElementById('global-dataset-select');
        if (!select) return;

        select.innerHTML = datasets.map(d => `
            <option value="${d.filename}" ${d.filename === active ? 'selected' : ''}>
                ${d.filename} (${d.size_kb} KB)
            </option>
        `).join('');

        // Remove old change listener and add new
        select.onchange = async (e) => {
            const filename = e.target.value;
            await this.switchActiveDataset(filename);
        };
    },

    async switchActiveDataset(filename) {
        this.showToast(`Loading dataset: ${filename}...`, 'info');
        try {
            const res = await fetch('/api/dataset/select', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ filename })
            });
            const data = await res.json();
            if (data.status === 'success') {
                this.activeDataset = filename;
                this.showToast(`Active dataset set to ${filename}`, 'success');
                this.refreshCurrentView();
            } else {
                this.showToast(data.message || 'Failed to switch dataset', 'error');
            }
        } catch (err) {
            console.error('Error switching dataset:', err);
            this.showToast('Network error switching dataset', 'error');
        }
    },

    navigateTo(route) {
        this.currentRoute = route;

        // Update nav active classes
        document.querySelectorAll('[data-route]').forEach(link => {
            const r = link.getAttribute('data-route');
            if (r === route) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });

        // Hide all views, display targeted view
        document.querySelectorAll('.module-view').forEach(view => {
            view.classList.add('hidden');
        });

        const activeView = document.getElementById(`view-${route}`);
        if (activeView) {
            activeView.classList.remove('hidden');
        }

        // Module lifecycle init
        this.refreshCurrentView();

        // Refresh icons
        if (window.lucide) window.lucide.createIcons();
    },

    refreshCurrentView() {
        switch (this.currentRoute) {
            case 'overview':
                OverviewModule.init();
                break;
            case 'datamanager':
                DataManagerModule.init();
                break;
            case 'sales':
                SalesAnalyticsModule.init();
                break;
            case 'products':
                ProductAnalyticsModule.init();
                break;
            case 'profit':
                ProfitAnalyticsModule.init();
                break;
            case 'ai-insights':
                AIInsightsModule.init();
                break;
            case 'reports':
                ReportsExportModule.init();
                break;
        }
    },

    showToast(message, type = 'info') {
        const container = document.getElementById('toast-container');
        if (!container) return;

        const toast = document.createElement('div');
        toast.className = `toast flex items-center gap-3 px-4 py-3 rounded-xl shadow-lg border text-sm max-w-sm ${
            type === 'success' ? 'bg-emerald-600 text-white border-emerald-500' :
            (type === 'error' ? 'bg-rose-600 text-white border-rose-500' :
            (type === 'warning' ? 'bg-amber-600 text-white border-amber-500' : 'bg-slate-800 text-white border-slate-700'))
        }`;

        let iconName = type === 'success' ? 'check-circle' : (type === 'error' ? 'alert-circle' : 'info');
        toast.innerHTML = `
            <i data-lucide="${iconName}" class="w-5 h-5 flex-shrink-0"></i>
            <span class="flex-1 font-medium">${message}</span>
        `;

        container.appendChild(toast);
        if (window.lucide) window.lucide.createIcons();

        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(10px)';
            toast.style.transition = 'all 0.3s ease';
            setTimeout(() => toast.remove(), 300);
        }, 3500);
    }
};

window.App = App;

// Bootstrap on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    App.init();
});
