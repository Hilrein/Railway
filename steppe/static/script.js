 // JavaScript для управления меню
 document.addEventListener("DOMContentLoaded", function () {
    const menuTrigger = document.getElementById("menu-trigger");
    const sideMenu = document.getElementById("side-menu");

    menuTrigger.addEventListener("click", function (e) {
        e.preventDefault(); // Отключить переход по ссылке
        sideMenu.classList.toggle("active");
    });

    // Закрыть меню, если нажали вне его области
    document.addEventListener("click", function (e) {
        if (!sideMenu.contains(e.target) && e.target !== menuTrigger) {
            sideMenu.classList.remove("active");
        }
    });
});