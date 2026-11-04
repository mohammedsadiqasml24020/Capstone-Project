/**
 * Module 5: Profit Analytics
 */
const ProfitAnalyticsModule = {
    async init() {
        await this.loadProfitData();
    },

    async loadProfitData() {
        try {
            const res = await fetch('/api/analytics/profit');
            const data = await res.json();
            if (data.status === 'success') {
                this.renderProfitKPIs(data);
                this.renderProfitabilityMatrix(data.profitability_matrix);
                this.renderComparisonChart(data.comparison_chart);
            }
        } catch (err) {
            console.error('ProfitAnalytics load error:', err);
        }
    },

    renderProfitKPIs(data) {
        // Total Profit
        const totEl = document.getElementById('profit-total-metric');
        if (totEl) totEl.innerText = '₹' + (data.total_profit || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 });

        // Average Profit
        const avgEl = document.getElementById('profit-avg-metric');
        if (avgEl) avgEl.innerText = '₹' + (data.average_profit || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 });

        // Overall Margin %
        const marginEl = document.getElementById('profit-margin-metric');
        if (marginEl) marginEl.innerText = `${data.overall_margin_pct || 0}%`;

        // Peak Single Profit
        const maxEl = document.getElementById('profit-max-metric');
        if (maxEl) maxEl.innerText = '₹' + (data.max_profit || 0).toLocaleString('en-IN');
    },

    renderProfitabilityMatrix(matrix) {
        const tbody = document.getElementById('profit-matrix-body');
        if (!tbody) return;

        if (!matrix || matrix.length === 0) {
            tbody.innerHTML = `<tr><td colspan="5" class="text-center py-6 text-slate-400">No profit records available in current dataset.</td></tr>`;
            return;
        }

        tbody.innerHTML = matrix.map(item => {
            let badgeClass = 'bg-slate-100 text-slate-700';
            if (item.badge_color === 'emerald') badgeClass = 'bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 font-semibold';
            else if (item.badge_color === 'blue') badgeClass = 'bg-blue-500/15 text-blue-600 dark:text-blue-400 font-semibold';
            else if (item.badge_color === 'amber') badgeClass = 'bg-amber-500/15 text-amber-600 dark:text-amber-400 font-semibold';
            else if (item.badge_color === 'rose') badgeClass = 'bg-rose-500/15 text-rose-600 dark:text-rose-400 font-semibold';

            return `
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition-colors border-b border-slate-100 dark:border-slate-800">
                    <td class="px-4 py-3 font-semibold text-slate-800 dark:text-slate-200">${item.product}</td>
                    <td class="px-4 py-3 text-slate-700 dark:text-slate-300 font-medium">₹${Number(item.sales).toLocaleString('en-IN')}</td>
                    <td class="px-4 py-3 text-emerald-600 dark:text-emerald-400 font-bold">₹${Number(item.profit).toLocaleString('en-IN')}</td>
                    <td class="px-4 py-3">
                        <span class="font-mono text-sm font-bold ${item.margin_pct >= 15 ? 'text-emerald-600 dark:text-emerald-400' : 'text-slate-600 dark:text-slate-300'}">
                            ${item.margin_pct}%
                        </span>
                    </td>
                    <td class="px-4 py-3">
                        <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs ${badgeClass}">
                            ${item.tier}
                        </span>
                    </td>
                </tr>
            `;
        }).join('');
    },

    renderComparisonChart(chartData) {
        if (!chartData || !chartData.labels || chartData.labels.length === 0) return;

        ChartManager.renderComboChart(
            'profit-combo-chart-canvas',
            chartData.labels,
            chartData.revenue,
            chartData.profit,
            {
                barLabel: 'Gross Revenue (₹)',
                lineLabel: 'Net Profit (₹)'
            }
        );
    }
};
