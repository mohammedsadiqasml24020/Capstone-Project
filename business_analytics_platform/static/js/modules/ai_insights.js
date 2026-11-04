/**
 * Module 6: AI Business Insights & Natural Language Assistant
 */
const AIInsightsModule = {
    chatHistory: [],

    async init() {
        this.bindEvents();
        await this.loadAutomatedInsights();
    },

    bindEvents() {
        const sendBtn = document.getElementById('ai-chat-send-btn');
        const inputField = document.getElementById('ai-chat-input');

        if (sendBtn && inputField) {
            sendBtn.addEventListener('click', () => this.handleSendMessage());
            inputField.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    this.handleSendMessage();
                }
            });
        }

        // Quick prompt chips
        document.querySelectorAll('.ai-prompt-chip').forEach(chip => {
            chip.addEventListener('click', () => {
                const query = chip.getAttribute('data-query');
                if (query && inputField) {
                    inputField.value = query;
                    this.handleSendMessage();
                }
            });
        });
    },

    async loadAutomatedInsights() {
        try {
            const res = await fetch('/api/ai/insights');
            const data = await res.json();
            if (data.status === 'success') {
                this.renderInsightsList(data.insights);
                this.renderAnomalies(data.anomalies);
                this.renderRecommendations(data.recommendations);
            }
        } catch (err) {
            console.error('AIInsights load error:', err);
        }
    },

    renderInsightsList(insights) {
        const container = document.getElementById('ai-insights-cards-container');
        if (!container) return;

        if (!insights || insights.length === 0) {
            container.innerHTML = `<div class="p-6 text-slate-400">No automated insights available.</div>`;
            return;
        }

        container.innerHTML = insights.map(item => `
            <div class="saas-card p-5 border-l-4 border-l-indigo-500 flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-xs font-bold uppercase tracking-wider text-indigo-600 dark:text-indigo-400 font-mono">${item.category}</span>
                        <span class="text-xs px-2 py-0.5 rounded-full font-semibold bg-indigo-500/10 text-indigo-600 dark:text-indigo-400">${item.impact}</span>
                    </div>
                    <h4 class="text-base font-bold text-slate-900 dark:text-white mb-1.5">${item.title}</h4>
                    <p class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">${item.description}</p>
                </div>
            </div>
        `).join('');
    },

    renderAnomalies(anomalies) {
        const container = document.getElementById('ai-anomalies-container');
        if (!container) return;

        if (!anomalies || anomalies.length === 0) {
            container.innerHTML = `
                <div class="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-700 dark:text-emerald-300 text-sm flex items-center gap-3">
                    <i data-lucide="check-circle" class="w-5 h-5 flex-shrink-0"></i>
                    <span><strong>Healthy Operational Status:</strong> No severe statistical anomalies or negative revenue outliers detected in active data.</span>
                </div>
            `;
            if (window.lucide) window.lucide.createIcons();
            return;
        }

        container.innerHTML = anomalies.map(a => `
            <div class="p-4 rounded-xl bg-amber-500/10 border border-amber-500/20 text-slate-800 dark:text-slate-200">
                <div class="flex items-center justify-between mb-1.5">
                    <span class="text-xs font-bold uppercase tracking-wider text-amber-600 dark:text-amber-400 flex items-center gap-1.5">
                        <i data-lucide="alert-triangle" class="w-4 h-4"></i> ${a.title}
                    </span>
                    <span class="text-xs px-2 py-0.5 rounded font-semibold bg-amber-500/20 text-amber-700 dark:text-amber-300">${a.severity}</span>
                </div>
                <p class="text-xs text-slate-600 dark:text-slate-300 mb-2">${a.description}</p>
                ${a.suggestion ? `<div class="text-xs font-medium text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950/40 p-2 rounded-lg"><strong>Recommendation:</strong> ${a.suggestion}</div>` : ''}
            </div>
        `).join('');

        if (window.lucide) window.lucide.createIcons();
    },

    renderRecommendations(recs) {
        const container = document.getElementById('ai-recommendations-container');
        if (!container) return;

        if (!recs || recs.length === 0) return;

        container.innerHTML = recs.map(r => `
            <div class="flex items-start gap-3 p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
                <span class="px-2 py-1 rounded text-[11px] font-bold font-mono bg-indigo-500/15 text-indigo-600 dark:text-indigo-400 flex-shrink-0">
                    ${r.priority}
                </span>
                <div>
                    <h5 class="text-xs font-bold text-slate-900 dark:text-white mb-0.5">${r.title}</h5>
                    <p class="text-xs text-slate-600 dark:text-slate-300">${r.action}</p>
                </div>
            </div>
        `).join('');
    },

    async handleSendMessage() {
        const inputField = document.getElementById('ai-chat-input');
        if (!inputField) return;

        const text = inputField.value.trim();
        if (!text) return;

        inputField.value = '';
        this.appendChatMessage('user', text);
        this.showTypingIndicator();

        try {
            const res = await fetch('/api/ai/ask', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: text })
            });
            const data = await res.json();
            this.hideTypingIndicator();

            if (data.status === 'success') {
                this.appendChatMessage('ai', data.result.answer, data.result.details);
            } else {
                this.appendChatMessage('ai', data.message || 'Sorry, I encountered an issue analyzing your query.');
            }
        } catch (err) {
            console.error('AI chat error:', err);
            this.hideTypingIndicator();
            this.appendChatMessage('ai', 'Error connecting to analytics engine. Please check server status.');
        }
    },

    appendChatMessage(sender, content, details = []) {
        const container = document.getElementById('ai-chat-messages');
        if (!container) return;

        const isUser = sender === 'user';
        const msgDiv = document.createElement('div');
        msgDiv.className = `flex gap-3 ${isUser ? 'justify-end' : 'justify-start'}`;

        let detailsHtml = '';
        if (details && details.length > 0) {
            detailsHtml = `
                <div class="mt-2.5 pt-2 border-t border-slate-200/40 dark:border-slate-700/40 space-y-1">
                    ${details.map(d => `<div class="text-xs font-mono text-slate-600 dark:text-slate-300 flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-indigo-500 flex-shrink-0"></span> ${d}</div>`).join('')}
                </div>
            `;
        }

        // Parse markdown bold **text**
        const formattedContent = content.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\n/g, '<br/>');

        msgDiv.innerHTML = isUser ? `
            <div class="max-w-[80%] bg-indigo-600 text-white p-3.5 rounded-2xl rounded-tr-none text-sm shadow-md">
                ${formattedContent}
            </div>
            <div class="w-8 h-8 rounded-full bg-indigo-500 text-white flex items-center justify-center font-bold text-xs flex-shrink-0">
                You
            </div>
        ` : `
            <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-indigo-500 to-blue-500 text-white flex items-center justify-center font-bold text-xs flex-shrink-0 shadow-md">
                AI
            </div>
            <div class="max-w-[85%] chat-bubble-ai p-4 rounded-2xl rounded-tl-none text-sm text-slate-800 dark:text-slate-200 shadow-sm leading-relaxed">
                ${formattedContent}
                ${detailsHtml}
            </div>
        `;

        container.appendChild(msgDiv);
        container.scrollTop = container.scrollHeight;
    },

    showTypingIndicator() {
        const container = document.getElementById('ai-chat-messages');
        if (!container) return;

        const typingDiv = document.createElement('div');
        typingDiv.id = 'ai-typing-indicator';
        typingDiv.className = 'flex gap-3 justify-start';
        typingDiv.innerHTML = `
            <div class="w-8 h-8 rounded-full bg-indigo-500 text-white flex items-center justify-center font-bold text-xs flex-shrink-0">
                AI
            </div>
            <div class="chat-bubble-ai p-3 rounded-2xl rounded-tl-none text-xs text-slate-500 flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-indigo-500 animate-bounce"></span>
                <span class="w-2 h-2 rounded-full bg-indigo-500 animate-bounce [animation-delay:0.2s]"></span>
                <span class="w-2 h-2 rounded-full bg-indigo-500 animate-bounce [animation-delay:0.4s]"></span>
                <span class="ml-1 text-slate-400 font-medium">Analyzing dataset...</span>
            </div>
        `;
        container.appendChild(typingDiv);
        container.scrollTop = container.scrollHeight;
    },

    hideTypingIndicator() {
        const el = document.getElementById('ai-typing-indicator');
        if (el) el.remove();
    }
};
