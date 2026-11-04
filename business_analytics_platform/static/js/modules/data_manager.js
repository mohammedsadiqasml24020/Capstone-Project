/**
 * Module 2: Data Upload & Management
 */
const DataManagerModule = {
    currentOverview: null,

    async init() {
        this.bindEvents();
        await this.loadOverview();
    },

    bindEvents() {
        const dropzone = document.getElementById('file-dropzone');
        const fileInput = document.getElementById('file-upload-input');

        if (dropzone && fileInput) {
            // Drag and drop events
            ['dragenter', 'dragover'].forEach(eventName => {
                dropzone.addEventListener(eventName, (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    dropzone.classList.add('drag-active');
                });
            });

            ['dragleave', 'drop'].forEach(eventName => {
                dropzone.addEventListener(eventName, (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    dropzone.classList.remove('drag-active');
                });
            });

            dropzone.addEventListener('drop', (e) => {
                const files = e.dataTransfer.files;
                if (files.length > 0) {
                    this.uploadFile(files[0]);
                }
            });

            fileInput.addEventListener('change', (e) => {
                if (e.target.files.length > 0) {
                    this.uploadFile(e.target.files[0]);
                }
            });
        }

        // Clean dataset button
        const cleanBtn = document.getElementById('btn-apply-cleaning');
        if (cleanBtn) {
            cleanBtn.addEventListener('click', () => this.applyCleaning());
        }

        // Reset dataset button
        const resetBtn = document.getElementById('btn-reset-dataset');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => this.resetDataset());
        }
    },

    async loadOverview() {
        try {
            const res = await fetch('/api/dataset/overview');
            const data = await res.json();
            if (data.status === 'success') {
                this.currentOverview = data;
                this.renderDatasetSummary(data);
                this.renderMissingValues(data.missing_values, data.total_rows);
                this.renderDuplicates(data.duplicate_rows);
                this.renderPreviewTable(data.columns, data.preview);
                this.renderStatisticalSummary(data.statistical_summary);
            }
        } catch (err) {
            console.error('Error loading dataset overview:', err);
        }
    },

    async uploadFile(file) {
        const formData = new FormData();
        formData.append('file', file);

        window.App.showToast(`Uploading ${file.name}...`, 'info');

        try {
            const res = await fetch('/api/dataset/upload', {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            if (data.status === 'success') {
                window.App.showToast(`Uploaded & Activated ${file.name}`, 'success');
                await window.App.refreshDatasetSelector();
                await this.loadOverview();
                window.App.refreshCurrentView();
            } else {
                window.App.showToast(data.message || 'Upload failed', 'error');
            }
        } catch (err) {
            console.error('Upload error:', err);
            window.App.showToast('Network error during upload', 'error');
        }
    },

    renderDatasetSummary(data) {
        const nameEl = document.getElementById('dm-dataset-name');
        if (nameEl) nameEl.innerText = data.active_dataset || 'No Dataset';

        const rowsEl = document.getElementById('dm-total-rows');
        if (rowsEl) rowsEl.innerText = data.total_rows.toLocaleString();

        const colsEl = document.getElementById('dm-total-cols');
        if (colsEl) colsEl.innerText = data.total_cols;

        const dupsEl = document.getElementById('dm-duplicate-count');
        if (dupsEl) dupsEl.innerText = data.duplicate_rows;
    },

    renderMissingValues(missingValues, totalRows) {
        const container = document.getElementById('dm-missing-container');
        if (!container) return;

        let totalMissing = 0;
        let html = '';

        for (const [col, info] of Object.entries(missingValues || {})) {
            totalMissing += info.count;
            const hasMissing = info.count > 0;
            html += `
                <div class="flex items-center justify-between p-3 rounded-xl ${hasMissing ? 'bg-amber-500/10 border border-amber-500/20' : 'bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800'}">
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full ${hasMissing ? 'bg-amber-500 animate-pulse' : 'bg-emerald-500'}"></span>
                        <span class="font-mono text-xs font-semibold text-slate-800 dark:text-slate-200">${col}</span>
                    </div>
                    <div class="text-right">
                        <span class="text-xs font-bold ${hasMissing ? 'text-amber-600 dark:text-amber-400' : 'text-slate-500'}">${info.count} missing</span>
                        <span class="text-[11px] text-slate-400 block">${info.percentage}%</span>
                    </div>
                </div>
            `;
        }

        const badge = document.getElementById('dm-total-missing-badge');
        if (badge) {
            badge.innerText = `${totalMissing} Total Missing Cells`;
            badge.className = `text-xs px-2.5 py-1 rounded-full font-semibold ${totalMissing > 0 ? 'bg-amber-500/15 text-amber-600 dark:text-amber-400' : 'bg-emerald-500/15 text-emerald-600 dark:text-emerald-400'}`;
        }

        container.innerHTML = html || '<div class="text-sm text-slate-400">No columns found.</div>';
    },

    renderDuplicates(duplicateCount) {
        const banner = document.getElementById('dm-duplicate-banner');
        if (!banner) return;

        if (duplicateCount > 0) {
            banner.classList.remove('hidden');
            const countText = document.getElementById('dm-duplicate-banner-count');
            if (countText) countText.innerText = duplicateCount;
        } else {
            banner.classList.add('hidden');
        }
    },

    renderPreviewTable(columns, previewRecords) {
        const thead = document.getElementById('dm-table-head');
        const tbody = document.getElementById('dm-table-body');
        if (!thead || !tbody) return;

        // Render header
        thead.innerHTML = columns.map(c => `
            <th class="px-4 py-3 text-left font-mono text-xs uppercase tracking-wider text-slate-500 dark:text-slate-400 font-semibold border-b border-slate-200 dark:border-slate-800">
                ${c}
            </th>
        `).join('');

        // Render records
        if (!previewRecords || previewRecords.length === 0) {
            tbody.innerHTML = `<tr><td colspan="${columns.length}" class="text-center py-6 text-slate-400">No records available.</td></tr>`;
            return;
        }

        tbody.innerHTML = previewRecords.map(row => `
            <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition-colors border-b border-slate-100 dark:border-slate-800/60">
                ${columns.map(c => {
                    const val = row[c];
                    const isNull = val === null || val === undefined;
                    return `
                        <td class="px-4 py-2.5 text-sm ${isNull ? 'text-amber-500 italic bg-amber-50/50 dark:bg-amber-950/20' : 'text-slate-700 dark:text-slate-300'}">
                            ${isNull ? 'null (missing)' : (typeof val === 'number' ? val.toLocaleString() : val)}
                        </td>
                    `;
                }).join('')}
            </tr>
        `).join('');
    },

    renderStatisticalSummary(stats) {
        const container = document.getElementById('dm-stats-summary-table');
        if (!container || !stats || Object.keys(stats).length === 0) return;

        const metrics = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'];
        const cols = Object.keys(stats);

        let html = `
            <table class="w-full text-left text-xs font-mono">
                <thead>
                    <tr class="border-b border-slate-200 dark:border-slate-800 text-slate-400">
                        <th class="py-2 px-3">Stat</th>
                        ${cols.map(c => `<th class="py-2 px-3 font-semibold text-slate-700 dark:text-slate-200">${c}</th>`).join('')}
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
        `;

        metrics.forEach(m => {
            html += `
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40">
                    <td class="py-2 px-3 uppercase text-slate-400 font-bold">${m}</td>
                    ${cols.map(c => {
                        const val = stats[c][m];
                        return `<td class="py-2 px-3 text-slate-600 dark:text-slate-300">${val !== null ? Number(val).toLocaleString() : '—'}</td>`;
                    }).join('')}
                </tr>
            `;
        });

        html += `</tbody></table>`;
        container.innerHTML = html;
    },

    async applyCleaning() {
        const strategySelect = document.getElementById('dm-clean-strategy');
        const strategy = strategySelect ? strategySelect.value : 'mean';
        const removeDupsCheck = document.getElementById('dm-clean-remove-duplicates');
        const removeDups = removeDupsCheck ? removeDupsCheck.checked : true;

        window.App.showToast('Cleaning dataset...', 'info');

        try {
            const res = await fetch('/api/dataset/clean', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    missing_strategy: strategy,
                    remove_duplicates: removeDups
                })
            });
            const data = await res.json();
            if (data.status === 'success') {
                const s = data.summary;
                window.App.showToast(`Cleaned: Filled ${s.missing_filled} missing values, removed ${s.duplicates_removed} duplicates`, 'success');
                await this.loadOverview();
                window.App.refreshCurrentView();
            } else {
                window.App.showToast(data.message || 'Cleaning failed', 'error');
            }
        } catch (err) {
            console.error('Cleaning error:', err);
            window.App.showToast('Network error during data cleaning', 'error');
        }
    },

    async resetDataset() {
        if (!confirm('Reset dataset back to its original unmodified raw state?')) return;
        window.App.showToast('Resetting dataset...', 'info');

        try {
            const res = await fetch('/api/dataset/reset', { method: 'POST' });
            const data = await res.json();
            if (data.status === 'success') {
                window.App.showToast('Dataset restored to raw state', 'success');
                await this.loadOverview();
                window.App.refreshCurrentView();
            } else {
                window.App.showToast(data.message || 'Reset failed', 'error');
            }
        } catch (err) {
            console.error('Reset error:', err);
            window.App.showToast('Network error resetting dataset', 'error');
        }
    }
};
