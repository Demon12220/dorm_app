// Функция для подтверждения удаления
function confirmDelete(event, message) {
    if (!confirm(message || 'Вы уверены?')) {
        event.preventDefault();
        return false;
    }
    return true;
}

// Инициализация всех подсказок Bootstrap
document.addEventListener('DOMContentLoaded', function() {
    // Инициализация тултипов
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Автоматическое скрытие flash-сообщений через 5 секунд
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert:not(.no-auto-close)');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            setTimeout(function() {
                bsAlert.close();
            }, 500);
        });
    }, 5000);

    // Если существует элемент с id roomStats (график статистики комнат)
    var roomStatsCanvas = document.getElementById('roomStats');
    if (roomStatsCanvas) {
        // Подключите Chart.js, если он не подключен
        if (typeof Chart === 'undefined') {
            var script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/chart.js';
            script.onload = initRoomStats;
            document.head.appendChild(script);
        } else {
            initRoomStats();
        }
    }

    // Обработчик для клика по строке таблицы
    var tableRows = document.querySelectorAll('.table-hover tr[data-href]');
    tableRows.forEach(function(row) {
        row.addEventListener('click', function() {
            window.location.href = this.dataset.href;
        });
    });
});

// Функция для инициализации графика статистики комнат
function initRoomStats() {
    var ctx = document.getElementById('roomStats').getContext('2d');
    var roomStats = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['1 этаж', '2 этаж', '3 этаж', '4 этаж', '5 этаж'],
            datasets: [{
                label: 'Занято комнат',
                data: [12, 19, 15, 17, 14],
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }, {
                label: 'Свободно комнат',
                data: [3, 5, 2, 4, 1],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
