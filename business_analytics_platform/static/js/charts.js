/**
 * Reusable Chart.js Manager with Dynamic Theme Adaptation (Light / Dark)
 */
const ChartManager = {
    instances: {},

    // Theme Colors
    getThemeColors() {
        const isDark = document.documentElement.classList.contains('dark');
        return {
            isDark,
            textColor: isDark ? '#cbd5e1' : '#475569',
            textMuted: isDark ? '#64748b' : '#94a3b8',
            gridColor: isDark ? 'rgba(255, 255, 255, 0.06)' : 'rgba(0, 0, 0, 0.06)',
            tooltipBg: isDark ? '#1e293b' : '#0f172a',
            tooltipText: '#ffffff',
            primary: '#6366f1',
            primaryLight: 'rgba(99, 102, 241, 0.15)',
            secondary: '#3b82f6',
            secondaryLight: 'rgba(59, 130, 246, 0.15)',
            emerald: '#10b981',
            emeraldLight: 'rgba(16, 185, 129, 0.15)',
            rose: '#f43f5e',
            roseLight: 'rgba(244, 63, 94, 0.15)',
            amber: '#f59e0b',
            palette: [
                '#6366f1', '#3b82f6', '#10b981', '#f59e0b', 
                '#ec4899', '#8b5cf6', '#14b8a6', '#f97316'
            ]
        };
    },

    destroy(chartId) {
        if (this.instances[chartId]) {
            this.instances[chartId].destroy();
            delete this.instances[chartId];
        }
    },

    // Destroy and re-render all active charts when dark mode toggles
    updateAllThemes() {
        // Re-triggers each active view's render functions
        if (window.App && typeof window.App.refreshCurrentView === 'function') {
            window.App.refreshCurrentView();
        }
    },

    // 1. Line / Area Chart
    renderLineChart(canvasId, labels, datasets, options = {}) {
        this.destroy(canvasId);
        const canvas = document.getElementById(canvasId);
        if (!canvas) return null;

        const colors = this.getThemeColors();
        const ctx = canvas.getContext('2d');

        const formattedDatasets = datasets.map((ds, idx) => {
            const baseColor = ds.color || colors.palette[idx % colors.palette.length];
            return {
                label: ds.label,
                data: ds.data,
                borderColor: baseColor,
                backgroundColor: ds.fill ? (ds.fillColor || colors.primaryLight) : 'transparent',
                fill: ds.fill ?? false,
                tension: ds.tension ?? 0.35,
                borderWidth: ds.borderWidth ?? 2.5,
                pointRadius: ds.pointRadius ?? 3.5,
                pointHoverRadius: 6,
                pointBackgroundColor: baseColor,
                pointBorderColor: '#ffffff',
                pointBorderWidth: 1.5
            };
        });

        this.instances[canvasId] = new Chart(ctx, {
            type: 'line',
            data: { labels, datasets: formattedDatasets },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: options.showLegend ?? true,
                        position: 'top',
                        labels: { color: colors.textColor, font: { family: 'Plus Jakarta Sans', size: 12 } }
                    },
                    tooltip: {
                        backgroundColor: colors.tooltipBg,
                        titleColor: colors.tooltipText,
                        bodyColor: colors.tooltipText,
                        borderColor: colors.gridColor,
                        borderWidth: 1,
                        padding: 10,
                        cornerRadius: 8,
                        callbacks: options.tooltipCallbacks || {}
                    }
                },
                scales: {
                    x: {
                        grid: { display: options.showGridX ?? false, color: colors.gridColor },
                        ticks: { color: colors.textMuted, font: { family: 'Plus Jakarta Sans', size: 11 } }
                    },
                    y: {
                        grid: { color: colors.gridColor },
                        ticks: {
                            color: colors.textMuted,
                            font: { family: 'Plus Jakarta Sans', size: 11 },
                            callback: options.yAxisCallback || ((val) => '₹' + Number(val).toLocaleString('en-IN'))
                        }
                    }
                }
            }
        });
        return this.instances[canvasId];
    },

    // 2. Bar Chart
    renderBarChart(canvasId, labels, datasets, options = {}) {
        this.destroy(canvasId);
        const canvas = document.getElementById(canvasId);
        if (!canvas) return null;

        const colors = this.getThemeColors();
        const ctx = canvas.getContext('2d');

        const formattedDatasets = datasets.map((ds, idx) => {
            const baseColor = ds.color || colors.palette[idx % colors.palette.length];
            return {
                label: ds.label,
                data: ds.data,
                backgroundColor: ds.backgroundColor || baseColor,
                borderColor: ds.borderColor || baseColor,
                borderWidth: 1,
                borderRadius: ds.borderRadius ?? 6,
                barPercentage: ds.barPercentage ?? 0.65,
                categoryPercentage: ds.categoryPercentage ?? 0.8
            };
        });

        this.instances[canvasId] = new Chart(ctx, {
            type: options.horizontal ? 'bar' : 'bar',
            data: { labels, datasets: formattedDatasets },
            options: {
                indexAxis: options.horizontal ? 'y' : 'x',
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: options.showLegend ?? false,
                        labels: { color: colors.textColor, font: { family: 'Plus Jakarta Sans', size: 12 } }
                    },
                    tooltip: {
                        backgroundColor: colors.tooltipBg,
                        titleColor: colors.tooltipText,
                        bodyColor: colors.tooltipText,
                        padding: 10,
                        cornerRadius: 8,
                        callbacks: options.tooltipCallbacks || {}
                    }
                },
                scales: {
                    x: {
                        grid: { display: options.showGridX ?? false, color: colors.gridColor },
                        ticks: {
                            color: colors.textMuted,
                            font: { family: 'Plus Jakarta Sans', size: 11 },
                            callback: options.horizontal ? ((val) => '₹' + Number(val).toLocaleString('en-IN')) : undefined
                        }
                    },
                    y: {
                        grid: { color: colors.gridColor },
                        ticks: {
                            color: colors.textMuted,
                            font: { family: 'Plus Jakarta Sans', size: 11 },
                            callback: !options.horizontal ? (options.yAxisCallback || ((val) => '₹' + Number(val).toLocaleString('en-IN'))) : undefined
                        }
                    }
                }
            }
        });
        return this.instances[canvasId];
    },

    // 3. Donut / Doughnut Chart
    renderDonutChart(canvasId, labels, data, options = {}) {
        this.destroy(canvasId);
        const canvas = document.getElementById(canvasId);
        if (!canvas) return null;

        const colors = this.getThemeColors();
        const ctx = canvas.getContext('2d');

        this.instances[canvasId] = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels,
                datasets: [{
                    data,
                    backgroundColor: options.colors || colors.palette.slice(0, labels.length),
                    borderWidth: 2,
                    borderColor: colors.isDark ? '#111827' : '#ffffff',
                    hoverOffset: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: options.cutout || '70%',
                plugins: {
                    legend: {
                        position: options.legendPosition || 'bottom',
                        labels: {
                            color: colors.textColor,
                            font: { family: 'Plus Jakarta Sans', size: 11 },
                            padding: 12,
                            usePointStyle: true,
                            pointStyle: 'circle'
                        }
                    },
                    tooltip: {
                        backgroundColor: colors.tooltipBg,
                        titleColor: colors.tooltipText,
                        bodyColor: colors.tooltipText,
                        padding: 10,
                        cornerRadius: 8,
                        callbacks: {
                            label: function(context) {
                                const val = context.raw || 0;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const pct = total > 0 ? ((val / total) * 100).toFixed(1) : 0;
                                return ` ${context.label}: ₹${Number(val).toLocaleString('en-IN')} (${pct}%)`;
                            }
                        }
                    }
                }
            }
        });
        return this.instances[canvasId];
    },

    // 4. Dual-Axis Bar & Line Combo Chart (Revenue vs Profit)
    renderComboChart(canvasId, labels, barData, lineData, options = {}) {
        this.destroy(canvasId);
        const canvas = document.getElementById(canvasId);
        if (!canvas) return null;

        const colors = this.getThemeColors();
        const ctx = canvas.getContext('2d');

        this.instances[canvasId] = new Chart(ctx, {
            type: 'bar',
            data: {
                labels,
                datasets: [
                    {
                        type: 'bar',
                        label: options.barLabel || 'Revenue (₹)',
                        data: barData,
                        backgroundColor: 'rgba(99, 102, 241, 0.75)',
                        borderColor: '#6366f1',
                        borderWidth: 1,
                        borderRadius: 6,
                        yAxisID: 'y'
                    },
                    {
                        type: 'line',
                        label: options.lineLabel || 'Profit (₹)',
                        data: lineData,
                        borderColor: '#10b981',
                        backgroundColor: 'rgba(16, 185, 129, 0.1)',
                        fill: false,
                        tension: 0.3,
                        borderWidth: 3,
                        pointRadius: 4,
                        pointBackgroundColor: '#10b981',
                        yAxisID: 'y1'
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                interaction: { mode: 'index', intersect: false },
                plugins: {
                    legend: {
                        position: 'top',
                        labels: { color: colors.textColor, font: { family: 'Plus Jakarta Sans', size: 12 } }
                    },
                    tooltip: {
                        backgroundColor: colors.tooltipBg,
                        titleColor: colors.tooltipText,
                        bodyColor: colors.tooltipText,
                        padding: 10,
                        cornerRadius: 8
                    }
                },
                scales: {
                    x: {
                        grid: { display: false },
                        ticks: { color: colors.textMuted, font: { family: 'Plus Jakarta Sans', size: 11 } }
                    },
                    y: {
                        type: 'linear',
                        display: true,
                        position: 'left',
                        grid: { color: colors.gridColor },
                        ticks: {
                            color: colors.textMuted,
                            font: { family: 'Plus Jakarta Sans', size: 11 },
                            callback: (v) => '₹' + Number(v).toLocaleString('en-IN')
                        }
                    },
                    y1: {
                        type: 'linear',
                        display: true,
                        position: 'right',
                        grid: { drawOnChartArea: false },
                        ticks: {
                            color: colors.textMuted,
                            font: { family: 'Plus Jakarta Sans', size: 11 },
                            callback: (v) => '₹' + Number(v).toLocaleString('en-IN')
                        }
                    }
                }
            }
        });
        return this.instances[canvasId];
    }
};
