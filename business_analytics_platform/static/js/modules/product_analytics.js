/**
 * Module 4: Product Analytics
 */
const ProductAnalyticsModule = {
    async init() {
        await this.loadProductData();
    },

    async loadProductData() {
        try {
            const res = await fetch('/api/analytics/products');
            const data = await res.json();
            if (data.status === 'success') {
                this.renderProductCards(data);
                this.renderProductCharts(data.chart_data);
                this.renderProductTable(data.product_list);
            } else if (data.status === 'warning') {
                window.App.showToast(data.message, 'warning');
                this.renderEmptyState();
            }
        } catch (err) {
            console.error('ProductAnalytics load error:', err);
        }
    },

    renderProductCards(data) {
        // Best Selling
        const best = data.best_selling;
        const bestNameEl = document.getElementById('prod-best-name');
        const bestRevEl = document.getElementById('prod-best-rev');
        const bestPctEl = document.getElementById('prod-best-pct');

        if (best && bestNameEl) {
            bestNameEl.innerText = best.product;
            if (bestRevEl) bestRevEl.innerText = '₹' + Number(best.sales).toLocaleString('en-IN');
            if (bestPctEl) bestPctEl.innerText = `${best.contribution}% of total catalog sales`;
        }

        // Least Selling
        const least = data.least_selling;
        const leastNameEl = document.getElementById('prod-least-name');
        const leastRevEl = document.getElementById('prod-least-rev');
        const leastPctEl = document.getElementById('prod-least-pct');

        if (least && leastNameEl) {
            leastNameEl.innerText = least.product;
            if (leastRevEl) leastRevEl.innerText = '₹' + Number(least.sales).toLocaleString('en-IN');
            if (leastPctEl) leastPctEl.innerText = `${least.contribution}% of total catalog sales`;
        }

        // Total Products Count
        const countEl = document.getElementById('prod-total-count');
        if (countEl) countEl.innerText = data.total_products || 0;
    },

    renderProductCharts(chartData) {
        if (!chartData || !chartData.labels || chartData.labels.length === 0) return;

        // 1. Horizontal Revenue Comparison Bar Chart
        const barDatasets = [
            {
                label: 'Revenue (₹)',
                data: chartData.sales,
                backgroundColor: 'rgba(99, 102, 241, 0.85)',
                borderColor: '#6366f1',
                borderRadius: 6
            }
        ];

        ChartManager.renderBarChart('prod-bar-chart-canvas', chartData.labels, barDatasets, {
            horizontal: true,
            showLegend: false
        });

        // 2. Interactive Contribution Percentage Donut Chart
        ChartManager.renderDonutChart('prod-donut-chart-canvas', chartData.labels, chartData.sales, {
            cutout: '68%',
            legendPosition: 'right'
        });
    },

    renderProductTable(products) {
        const tbody = document.getElementById('prod-table-body');
        if (!tbody) return;

        if (!products || products.length === 0) {
            tbody.innerHTML = `<tr><td colspan="6" class="text-center py-6 text-slate-400">No product records found.</td></tr>`;
            return;
        }

        tbody.innerHTML = products.map((p, i) => {
            const rankBadge = i === 0 ? 'bg-amber-500/15 text-amber-600 dark:text-amber-400 font-bold' :
                             (i === 1 ? 'bg-slate-300/40 text-slate-700 dark:text-slate-300 font-semibold' :
                             (i === 2 ? 'bg-amber-700/15 text-amber-700 dark:text-amber-500 font-semibold' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'));

            return `
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition-colors border-b border-slate-100 dark:border-slate-800">
                    <td class="px-4 py-3 text-center">
                        <span class="inline-flex items-center justify-center w-6 h-6 rounded-full text-xs ${rankBadge}">
                            #${p.rank}
                        </span>
                    </td>
                    <td class="px-4 py-3 font-semibold text-slate-800 dark:text-slate-200">
                        ${p.product}
                    </td>
                    <td class="px-4 py-3 font-bold text-slate-900 dark:text-white">
                        ₹${Number(p.sales).toLocaleString('en-IN')}
                    </td>
                    <td class="px-4 py-3 text-emerald-600 dark:text-emerald-400 font-semibold">
                        ₹${Number(p.profit).toLocaleString('en-IN')}
                    </td>
                    <td class="px-4 py-3 text-slate-600 dark:text-slate-300">
                        <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-semibold ${p.profit_margin_pct >= 15 ? 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-400' : 'bg-slate-100 dark:bg-slate-800 text-slate-600'}">
                            ${p.profit_margin_pct}%
                        </span>
                    </td>
                    <td class="px-4 py-3">
                        <div class="flex items-center gap-2">
                            <div class="w-24 bg-slate-200 dark:bg-slate-700 rounded-full h-2 overflow-hidden">
                                <div class="bg-indigo-600 h-2 rounded-full" style="width: ${Math.min(100, p.contribution_pct)}%"></div>
                            </div>
                            <span class="text-xs font-medium text-slate-500">${p.contribution_pct}%</span>
                        </div>
                    </td>
                </tr>
            `;
        }).join('');
    },

    renderEmptyState() {
        const tbody = document.getElementById('prod-table-body');
        if (tbody) tbody.innerHTML = `<tr><td colspan="6" class="text-center py-6 text-slate-400">No product column detected in the active dataset. Upload a dataset with a 'Product' column to view full breakdown.</td></tr>`;
    }
};
