/**
 * Module 7: Reports & Export
 */
const ReportsExportModule = {
    reportData: null,

    async init() {
        this.bindEvents();
        await this.loadReportData();
    },

    bindEvents() {
        // PDF Export / Print
        const printBtn = document.getElementById('report-export-pdf-btn');
        if (printBtn) {
            printBtn.addEventListener('click', () => {
                window.print();
            });
        }

        // CSV Export
        const csvBtn = document.getElementById('report-export-csv-btn');
        if (csvBtn) {
            csvBtn.addEventListener('click', () => {
                window.location.href = '/api/dataset/export/csv';
            });
        }

        // Excel Export
        const excelBtn = document.getElementById('report-export-excel-btn');
        if (excelBtn) {
            excelBtn.addEventListener('click', () => {
                window.location.href = '/api/dataset/export/excel';
            });
        }

        // Refresh Report Data
        const refreshBtn = document.getElementById('report-refresh-btn');
        if (refreshBtn) {
            refreshBtn.addEventListener('click', () => {
                this.loadReportData();
                window.App.showToast('Report updated with latest metrics', 'success');
            });
        }
    },

    async loadReportData() {
        try {
            const res = await fetch('/api/reports/analytical');
            const data = await res.json();
            if (data.status === 'success') {
                this.reportData = data.report;
                this.renderReportView(data.report);
            }
        } catch (err) {
            console.error('Error loading report:', err);
        }
    },

    renderReportView(report) {
        const titleEl = document.getElementById('report-doc-title');
        const timeEl = document.getElementById('report-doc-time');
        const datasetEl = document.getElementById('report-doc-dataset');

        if (titleEl) titleEl.innerText = report.title;
        if (timeEl) timeEl.innerText = report.generation_time;
        if (datasetEl) datasetEl.innerText = report.dataset_analyzed;

        // Executive Metrics
        const exec = report.executive_summary;
        const grid = document.getElementById('report-exec-summary-grid');
        if (grid && exec) {
            grid.innerHTML = `
                <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
                    <span class="text-xs text-slate-400 font-medium block">Total Revenue</span>
                    <span class="text-lg font-bold text-slate-900 dark:text-white">₹${Number(exec.total_revenue).toLocaleString('en-IN', { minimumFractionDigits: 2 })}</span>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
                    <span class="text-xs text-slate-400 font-medium block">Total Profit</span>
                    <span class="text-lg font-bold text-emerald-600 dark:text-emerald-400">₹${Number(exec.total_profit).toLocaleString('en-IN', { minimumFractionDigits: 2 })}</span>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
                    <span class="text-xs text-slate-400 font-medium block">Net Margin</span>
                    <span class="text-lg font-bold text-indigo-600 dark:text-indigo-400">${exec.profit_margin}%</span>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
                    <span class="text-xs text-slate-400 font-medium block">Average Sale</span>
                    <span class="text-lg font-bold text-slate-900 dark:text-white">₹${Number(exec.average_sale).toLocaleString('en-IN', { minimumFractionDigits: 2 })}</span>
                </div>
            `;
        }

        // Leaderboard table
        const leadTbody = document.getElementById('report-leaderboard-body');
        if (leadTbody && report.product_leaderboard) {
            leadTbody.innerHTML = report.product_leaderboard.map(p => `
                <tr class="border-b border-slate-100 dark:border-slate-800">
                    <td class="py-2.5 px-3 font-semibold text-slate-800 dark:text-slate-200">${p.product}</td>
                    <td class="py-2.5 px-3 text-slate-900 dark:text-white font-bold">₹${Number(p.sales).toLocaleString('en-IN')}</td>
                    <td class="py-2.5 px-3 text-emerald-600 font-semibold">₹${Number(p.profit).toLocaleString('en-IN')}</td>
                    <td class="py-2.5 px-3 font-mono text-xs font-bold text-indigo-600 dark:text-indigo-400">${p.profit_margin_pct}%</td>
                    <td class="py-2.5 px-3 text-slate-500">${p.contribution_pct}%</td>
                </tr>
            `).join('');
        }

        // AI Recommendations list in report
        const recList = document.getElementById('report-recommendations-list');
        if (recList && report.recommendations) {
            recList.innerHTML = report.recommendations.map(r => `
                <li class="flex items-start gap-2 text-xs text-slate-700 dark:text-slate-300">
                    <span class="w-1.5 h-1.5 rounded-full bg-indigo-500 mt-1.5 flex-shrink-0"></span>
                    <span><strong>${r.title}:</strong> ${r.action}</span>
                </li>
            `).join('');
        }
    }
};
