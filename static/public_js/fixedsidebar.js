$("body").addClass('fixed-sidebar');
$('.sidebar-collapse').slimScroll({
    height: '100%',
    railOpacity: 0.9
});

if (localStorageSupport) {
    localStorage.setItem("fixedsidebar", 'on');
}