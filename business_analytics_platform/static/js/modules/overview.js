/**
 * Module 1: Overview Dashboard
 */
const OverviewModule = {
    async init() {
        await this.loadData();
    },

    async loadData() {
        try {
            const res = await fetch('/api/analytics/overview');
            const data = await res.json();
            if (data.status === 'success') {
                this.renderKPIs(data.data);
                this.renderPerformanceChart(data.data.chart_preview);
                this.renderRecentActivities(data.data.recent_records);
            } else {
                window.App.showToast('Error loading overview data', 'error');
            }
        } catch (err) {
            console.error('OverviewModule load error:', err);
            window.App.showToast('Network error loading overview', 'error');
        }
    },

    renderKPIs(kpis) {
        // Total Revenue
        const revEl = document.getElementById('kpi-revenue');
        if (revEl) revEl.innerText = '₹' + (kpis.total_revenue || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 });

        // Revenue Growth Pill
        const growthEl = document.getElementById('kpi-revenue-growth');
        if (growthEl) {
            const g = kpis.revenue_growth || 0;
            const isPos = g >= 0;
            growthEl.className = `inline-flex items-center gap-1 text-xs font-semibold px-2.5 py-0.5 rounded-full ${isPos ? 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-400' : 'bg-rose-500/10 text-rose-600 dark:text-rose-400'}`;
            growthEl.innerHTML = `<i data-lucide="${isPos ? 'trending-up' : 'trending-down'}" class="w-3.5 h-3.5"></i> ${isPos ? '+' : ''}${g}%`;
        }

        // Total Sales Count
        const countEl = document.getElementById('kpi-sales-count');
        if (countEl) countEl.innerText = (kpis.total_sales_count || 0).toLocaleString('en-IN');

        // Total Profit
        const profitEl = document.getElementById('kpi-profit');
        if (profitEl) profitEl.innerText = '₹' + (kpis.total_profit || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 });

        // Profit Margin Pill
        const marginEl = document.getElementById('kpi-profit-margin');
        if (marginEl) {
            marginEl.innerText = `${kpis.profit_margin || 0}% margin`;
        }

        // Average Sales
        const avgEl = document.getElementById('kpi-avg-sales');
        if (avgEl) avgEl.innerText = '₹' + (kpis.average_sales || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 });

        // Total Products
        const prodEl = document.getElementById('kpi-products');
        if (prodEl) prodEl.innerText = (kpis.total_products || 1).toLocaleString();

        // Correlation Badge
        const corrEl = document.getElementById('kpi-correlation');
        if (corrEl) {
            if (kpis.correlation !== null && kpis.correlation !== undefined) {
                corrEl.innerText = `r = ${kpis.correlation} (High correlation)`;
            } else {
                corrEl.innerText = `N/A`;
            }
        }

        // Refresh Lucide icons inside newly rendered elements
        if (window.lucide) window.lucide.createIcons();
    },

    renderPerformanceChart(chartData) {
        if (!chartData || !chartData.labels || chartData.labels.length === 0) return;

        const datasets = [
            {
                label: 'Sales Revenue',
                data: chartData.sales,
                color: '#6366f1',
                fill: true,
                fillColor: 'rgba(99, 102, 241, 0.12)'
            }
        ];

        if (chartData.profit && chartData.profit.length > 0) {
            datasets.push({
                label: 'Net Profit',
                data: chartData.profit,
                color: '#10b981',
                fill: false
            });
        }

        ChartManager.renderLineChart('overview-chart-canvas', chartData.labels, datasets, {
            showLegend: true,
            yAxisCallback: (val) => '₹' + (val >= 10000000 ? (val / 10000000).toFixed(1) + 'Cr' : (val >= 100000 ? (val / 100000).toFixed(1) + 'L' : (val >= 1000 ? (val / 1000).toFixed(0) + 'k' : val)))
        });
    },

    renderRecentActivities(records) {
        const container = document.getElementById('overview-recent-table-body');
        if (!container) return;

        if (!records || records.length === 0) {
            container.innerHTML = `<tr><td colspan="5" class="text-center py-6 text-slate-400">No records to display.</td></tr>`;
            return;
        }

        container.innerHTML = records.map((r, i) => {
            const dateVal = r.Date || r.Month || `Entry #${i+1}`;
            const prodVal = r.Product || r.Category || 'General Goods';
            const salesVal = r.Sales !== null && r.Sales !== undefined ? '₹' + Number(r.Sales).toLocaleString('en-IN') : 'N/A';
            const profitVal = r.Profit !== null && r.Profit !== undefined ? '₹' + Number(r.Profit).toLocaleString('en-IN') : '—';
            
            return `
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition-colors">
                    <td class="font-medium text-slate-800 dark:text-slate-200">${dateVal}</td>
                    <td class="text-slate-600 dark:text-slate-300">
                        <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-medium bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                            <span class="w-1.5 h-1.5 rounded-full bg-indigo-500"></span>
                            ${prodVal}
                        </span>
                    </td>
                    <td class="font-semibold text-slate-900 dark:text-white">${salesVal}</td>
                    <td class="font-medium text-emerald-600 dark:text-emerald-400">${profitVal}</td>
                    <td>
                        <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400">
                            <i data-lucide="check" class="w-3 h-3"></i> Verified
                        </span>
                    </td>
                </tr>
            `;
        }).join('');

        if (window.lucide) window.lucide.createIcons();
    }
};
