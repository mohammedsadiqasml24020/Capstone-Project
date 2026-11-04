/**
 * Module 3: Sales Analytics
 */
const SalesAnalyticsModule = {
    currentData: null,

    async init() {
        this.bindEvents();
        await this.loadSalesData();
    },

    bindEvents() {
        const filterBtn = document.getElementById('sales-filter-apply-btn');
        if (filterBtn) {
            filterBtn.addEventListener('click', () => {
                const dateFrom = document.getElementById('sales-date-from')?.value;
                const dateTo = document.getElementById('sales-date-to')?.value;
                this.loadSalesData(dateFrom, dateTo);
            });
        }

        const resetFilterBtn = document.getElementById('sales-filter-reset-btn');
        if (resetFilterBtn) {
            resetFilterBtn.addEventListener('click', () => {
                const df = document.getElementById('sales-date-from');
                const dt = document.getElementById('sales-date-to');
                if (df) df.value = '';
                if (dt) dt.value = '';
                this.loadSalesData();
            });
        }
    },

    async loadSalesData(dateFrom = '', dateTo = '') {
        try {
            let url = '/api/analytics/sales';
            const params = new URLSearchParams();
            if (dateFrom) params.append('from', dateFrom);
            if (dateTo) params.append('to', dateTo);
            if (params.toString()) url += '?' + params.toString();

            const res = await fetch(url);
            const data = await res.json();
            if (data.status === 'success') {
                this.currentData = data;
                this.renderSummaryKPIs(data);
                this.renderMonthlyChart(data.monthly_analysis);
                this.renderCumulativeTrendChart(data.monthly_analysis);
                this.renderDailyChart(data.daily_analysis);
            } else {
                window.App.showToast(data.error || 'Failed to load sales analytics', 'error');
            }
        } catch (err) {
            console.error('SalesAnalytics load error:', err);
        }
    },

    renderSummaryKPIs(data) {
        // Total filtered sales
        const totEl = document.getElementById('sales-total-amount');
        if (totEl) totEl.innerText = '₹' + (data.total_sales || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 });

        // Period Average
        const avgEl = document.getElementById('sales-average-amount');
        if (avgEl) avgEl.innerText = '₹' + (data.average_period_sales || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 });

        // Overall Growth
        const growthEl = document.getElementById('sales-overall-growth');
        if (growthEl) {
            const g = data.overall_growth_percentage || 0;
            const isPos = g >= 0;
            growthEl.innerHTML = `<span class="${isPos ? 'text-emerald-500' : 'text-rose-500'} font-bold">${isPos ? '+' : ''}${g}%</span> Overall Trend`;
        }

        // Peak Period Card
        const peakEl = document.getElementById('sales-peak-period-name');
        const peakValEl = document.getElementById('sales-peak-period-val');
        if (peakEl && data.highest_sales_period) {
            peakEl.innerText = data.highest_sales_period.period;
            if (peakValEl) peakValEl.innerText = '₹' + (data.highest_sales_period.sales || 0).toLocaleString('en-IN');
        }

        // Lowest Period Card
        const lowEl = document.getElementById('sales-low-period-name');
        const lowValEl = document.getElementById('sales-low-period-val');
        if (lowEl && data.lowest_sales_period) {
            lowEl.innerText = data.lowest_sales_period.period;
            if (lowValEl) lowValEl.innerText = '₹' + (data.lowest_sales_period.sales || 0).toLocaleString('en-IN');
        }
    },

    renderMonthlyChart(monthly) {
        if (!monthly || !monthly.labels || monthly.labels.length === 0) return;

        const datasets = [
            {
                label: 'Monthly Revenue (₹)',
                data: monthly.sales,
                backgroundColor: 'rgba(99, 102, 241, 0.85)',
                borderColor: '#6366f1',
                borderRadius: 8
            }
        ];

        ChartManager.renderBarChart('sales-monthly-chart-canvas', monthly.labels, datasets, {
            showLegend: false,
            yAxisCallback: (val) => '₹' + (val >= 10000000 ? (val / 10000000).toFixed(1) + 'Cr' : (val >= 100000 ? (val / 100000).toFixed(1) + 'L' : (val >= 1000 ? (val / 1000).toFixed(0) + 'k' : val)))
        });
    },

    renderCumulativeTrendChart(monthly) {
        if (!monthly || !monthly.labels || monthly.labels.length === 0) return;

        const datasets = [
            {
                label: 'Cumulative Revenue Progression (₹)',
                data: monthly.cumulative,
                color: '#3b82f6',
                fill: true,
                fillColor: 'rgba(59, 130, 246, 0.12)',
                tension: 0.4
            }
        ];

        ChartManager.renderLineChart('sales-cumulative-chart-canvas', monthly.labels, datasets, {
            showLegend: true,
            yAxisCallback: (val) => '₹' + (val >= 10000000 ? (val / 10000000).toFixed(1) + 'Cr' : (val >= 100000 ? (val / 100000).toFixed(1) + 'L' : (val >= 1000 ? (val / 1000).toFixed(0) + 'k' : val)))
        });
    },

    renderDailyChart(daily) {
        if (!daily || !daily.labels || daily.labels.length === 0) return;

        const datasets = [
            {
                label: 'Timeline Sales Performance (₹)',
                data: daily.sales,
                color: '#10b981',
                fill: false,
                borderWidth: 2,
                pointRadius: daily.labels.length > 20 ? 2 : 4
            }
        ];

        ChartManager.renderLineChart('sales-daily-chart-canvas', daily.labels, datasets, {
            showLegend: false,
            yAxisCallback: (val) => '₹' + (val >= 10000000 ? (val / 10000000).toFixed(1) + 'Cr' : (val >= 100000 ? (val / 100000).toFixed(1) + 'L' : (val >= 1000 ? (val / 1000).toFixed(0) + 'k' : val)))
        });
    }
};
