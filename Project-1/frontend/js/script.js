/* ============================================
   ATM Banking System - JavaScript Application
   ============================================ */

// API Configuration
const API_BASE_URL = window.location.origin;

// Current Session
let currentSession = {
    account: null,
    pin: null,
    name: null
};

// ============================================
// Notification System
// ============================================
function showNotification(message, type = 'success') {
    const notification = document.getElementById('notification');
    const messageEl = document.getElementById('notification-message');

    notification.className = `notification ${type}`;
    messageEl.textContent = message;
    notification.classList.add('show');
    notification.classList.remove('hidden');

    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => notification.classList.add('hidden'), 300);
    }, 4000);
}

// ============================================
// Loading State
// ============================================
function showLoading() {
    document.getElementById('loading-overlay').classList.remove('hidden');
}

function hideLoading() {
    document.getElementById('loading-overlay').classList.add('hidden');
}

// ============================================
// Tab Navigation
// ============================================
document.addEventListener('DOMContentLoaded', () => {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Update active tab
            tabButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Show appropriate form
            const tab = btn.dataset.tab;
            if (tab === 'login') {
                loginForm.classList.add('active');
                registerForm.classList.remove('active');
            } else {
                loginForm.classList.remove('active');
                registerForm.classList.add('active');
            }
        });
    });

    // Check for saved session
    const savedSession = sessionStorage.getItem('atmSession');
    if (savedSession) {
        currentSession = JSON.parse(savedSession);
        showDashboard();
        checkBalance();
    }
});

// ============================================
// Account Creation
// ============================================
async function createAccount(event) {
    event.preventDefault();

    const account = parseInt(document.getElementById('reg-account').value);
    const name = document.getElementById('reg-name').value.trim();
    const pin = parseInt(document.getElementById('reg-pin').value);
    const bank = document.getElementById('reg-bank').value.trim();
    const address = document.getElementById('reg-address').value.trim();
    const balance = parseFloat(document.getElementById('reg-balance').value);

    // Validation
    if (isNaN(account) || account < 10000) {
        showNotification('Account number must be at least 5 digits', 'error');
        return;
    }

    if (name.length < 2) {
        showNotification('Please enter a valid name', 'error');
        return;
    }

    if (isNaN(pin) || pin < 1000 || pin > 9999) {
        showNotification('PIN must be exactly 4 digits', 'error');
        return;
    }

    if (isNaN(balance) || balance < 0) {
        showNotification('Initial deposit must be 0 or greater', 'error');
        return;
    }

    showLoading();

    try {
        const response = await fetch(`${API_BASE_URL}/bankdata`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                account,
                name,
                pin,
                bank_name: bank,
                address,
                balance
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Failed to create account');
        }

        const data = await response.json();
        hideLoading();

        showNotification('Account created successfully! Please login.', 'success');

        // Clear form
        document.getElementById('register-form').querySelector('form').reset();

        // Switch to login tab
        document.getElementById('login-tab-btn').click();
        document.getElementById('login-account').value = account;

    } catch (error) {
        hideLoading();
        console.error('Create account error:', error);

        if (error.message.includes('fetch')) {
            showNotification('Cannot connect to server. Please ensure backend is running.', 'error');
        } else {
            showNotification(error.message || 'Failed to create account', 'error');
        }
    }
}

// ============================================
// Login
// ============================================
async function login(event) {
    event.preventDefault();

    const account = parseInt(document.getElementById('login-account').value);
    const pin = parseInt(document.getElementById('login-pin').value);

    if (isNaN(account) || account <= 0) {
        showNotification('Please enter a valid account number', 'error');
        return;
    }

    if (isNaN(pin) || pin < 1000 || pin > 999999) {
        showNotification('Please enter a valid PIN (4-6 digits)', 'error');
        return;
    }

    showLoading();

    try {
        // Verify credentials by checking balance
        const response = await fetch(`${API_BASE_URL}/atm/balance/${account}/${pin}`);
        const data = await response.json();

        hideLoading();

        if (response.ok) {
            // Get account details for name
            const accountResponse = await fetch(`${API_BASE_URL}/get_account/${account}`);
            const accountData = await accountResponse.json();

            // Save session
            currentSession = {
                account,
                pin,
                name: accountData?.name || 'User'
            };
            sessionStorage.setItem('atmSession', JSON.stringify(currentSession));

            showNotification('Login successful!', 'success');
            showDashboard();
            updateBalance(data.balance);

        } else {
            showNotification(data.detail || data.error || 'Invalid account or PIN', 'error');
        }

    } catch (error) {
        hideLoading();
        console.error('Login error:', error);
        showNotification('Cannot connect to server. Please ensure backend is running.', 'error');
    }
}

// ============================================
// Show Dashboard
// ============================================
function showDashboard() {
    document.getElementById('auth-section').classList.add('hidden');
    document.getElementById('dashboard-section').classList.remove('hidden');
    document.getElementById('user-name').textContent = currentSession.name || 'User';
}

// ============================================
// Logout
// ============================================
function logout() {
    currentSession = { account: null, pin: null, name: null };
    sessionStorage.removeItem('atmSession');

    document.getElementById('dashboard-section').classList.add('hidden');
    document.getElementById('auth-section').classList.remove('hidden');

    // Clear forms
    document.getElementById('login-account').value = '';
    document.getElementById('login-pin').value = '';
    document.getElementById('withdraw-amount').value = '';
    document.getElementById('deposit-amount').value = '';

    showNotification('Logged out successfully', 'success');
}

// ============================================
// Update Balance Display
// ============================================
function updateBalance(balance) {
    const balanceDisplay = document.getElementById('balance-display');
    const formattedBalance = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(balance);

    balanceDisplay.textContent = formattedBalance;

    // Add animation
    balanceDisplay.style.transform = 'scale(1.05)';
    setTimeout(() => {
        balanceDisplay.style.transform = 'scale(1)';
    }, 200);
}

// ============================================
// Check Balance
// ============================================
async function checkBalance() {
    if (!currentSession.account) return;

    showLoading();

    try {
        const response = await fetch(
            `${API_BASE_URL}/atm/balance/${currentSession.account}/${currentSession.pin}`
        );
        const data = await response.json();

        hideLoading();

        if (response.ok) {
            updateBalance(data.balance);
            showNotification('Balance updated!', 'success');
        } else {
            showNotification(data.detail || data.error || 'Failed to fetch balance', 'error');
        }

    } catch (error) {
        hideLoading();
        console.error('Check balance error:', error);
        showNotification('Cannot connect to server', 'error');
    }
}

// ============================================
// Withdraw
// ============================================
async function withdraw(event) {
    event.preventDefault();

    const amountInput = document.getElementById('withdraw-amount');
    const amount = parseFloat(amountInput.value);

    if (isNaN(amount) || amount <= 0) {
        showNotification('Please enter a valid amount', 'error');
        return;
    }

    showLoading();

    try {
        const response = await fetch(
            `${API_BASE_URL}/atm/withdraw?account=${currentSession.account}&pin=${currentSession.pin}&amount=${amount}`,
            { method: 'POST' }
        );
        const data = await response.json();

        hideLoading();

        if (response.ok) {
            updateBalance(data.new_balance);
            showNotification(`Successfully withdrew $${amount.toFixed(2)}`, 'success');
            amountInput.value = '';
        } else {
            showNotification(data.detail || data.error || 'Withdrawal failed', 'error');
        }

    } catch (error) {
        hideLoading();
        console.error('Withdraw error:', error);
        showNotification('Cannot connect to server', 'error');
    }
}

// ============================================
// Deposit
// ============================================
async function deposit(event) {
    event.preventDefault();

    const amountInput = document.getElementById('deposit-amount');
    const amount = parseFloat(amountInput.value);

    if (isNaN(amount) || amount <= 0) {
        showNotification('Please enter a valid amount', 'error');
        return;
    }

    showLoading();

    try {
        const response = await fetch(
            `${API_BASE_URL}/atm/deposit?account=${currentSession.account}&pin=${currentSession.pin}&amount=${amount}`,
            { method: 'POST' }
        );
        const data = await response.json();

        hideLoading();

        if (response.ok) {
            updateBalance(data.new_balance);
            showNotification(`Successfully deposited $${amount.toFixed(2)}`, 'success');
            amountInput.value = '';
        } else {
            showNotification(data.detail || data.error || 'Deposit failed', 'error');
        }

    } catch (error) {
        hideLoading();
        console.error('Deposit error:', error);
        showNotification('Cannot connect to server', 'error');
    }
}

// ============================================
// Transaction History
// ============================================
async function showTransactions() {
    showLoading();

    try {
        const response = await fetch(
            `${API_BASE_URL}/atm/transactions/${currentSession.account}/${currentSession.pin}`
        );
        const data = await response.json();

        hideLoading();

        if (response.ok) {
            renderTransactions(data.transactions);
            document.getElementById('transaction-modal').classList.remove('hidden');
        } else {
            showNotification(data.detail || data.error || 'Failed to fetch transactions', 'error');
        }

    } catch (error) {
        hideLoading();
        console.error('Get transactions error:', error);
        showNotification('Cannot connect to server', 'error');
    }
}

function renderTransactions(transactions) {
    const container = document.getElementById('transactions-list');

    if (!transactions || transactions.length === 0) {
        container.innerHTML = `
            <div class="no-transactions">
                <p>📭 No transactions yet</p>
            </div>
        `;
        return;
    }

    // Sort by most recent first
    const sortedTransactions = [...transactions].reverse();

    container.innerHTML = sortedTransactions.map(trans => {
        const isCredit = trans.type === 'credit';
        const formattedAmount = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }).format(trans.amount);

        const formattedBalance = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }).format(trans.balance_after);

        const date = new Date(trans.timestamp);
        const formattedDate = date.toLocaleString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });

        return `
            <div class="transaction-item">
                <div class="transaction-info">
                    <span class="transaction-type ${trans.type}">
                        ${isCredit ? '💰 Deposit' : '💸 Withdrawal'}
                    </span>
                    <span class="transaction-date">${formattedDate}</span>
                    <span class="transaction-date">Balance after: ${formattedBalance}</span>
                </div>
                <span class="transaction-amount ${trans.type}">
                    ${isCredit ? '+' : '-'}${formattedAmount}
                </span>
            </div>
        `;
    }).join('');
}

function closeModal() {
    document.getElementById('transaction-modal').classList.add('hidden');
}

// Close modal on outside click
document.getElementById('transaction-modal')?.addEventListener('click', (e) => {
    if (e.target.id === 'transaction-modal') {
        closeModal();
    }
});

// Close modal on ESC key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeModal();
    }
});
