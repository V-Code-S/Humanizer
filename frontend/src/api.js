const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

class ApiClient {
    async humanizeText(text, style = 'default') {
        try {
            const response = await fetch(`${API_BASE_URL}/humanize`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    text,
                    style,
                }),
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.detail || 'Failed to humanize text');
            }

            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    async bulkHumanize(texts, style = 'default') {
        try {
            const response = await fetch(`${API_BASE_URL}/humanize/bulk`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    texts,
                    style,
                }),
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.detail || 'Failed to bulk humanize texts');
            }

            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    async getStyles() {
        try {
            const response = await fetch(`${API_BASE_URL}/styles`);

            if (!response.ok) {
                throw new Error('Failed to fetch styles');
            }

            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    async analyzeText(text, style = 'default') {
        try {
            const response = await fetch(`${API_BASE_URL}/analyze`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    text,
                    style,
                }),
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.detail || 'Failed to analyze text');
            }

            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    async healthCheck() {
        try {
            const response = await fetch(API_BASE_URL.replace('/api', '') + '/health');
            return response.ok;
        } catch {
            return false;
        }
    }
}

export default new ApiClient();
