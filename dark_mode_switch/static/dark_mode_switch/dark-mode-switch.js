function getSystemColorScheme() {
  if (window.matchMedia) {
    if(window.matchMedia('(prefers-color-scheme: dark)').matches){
      return 'dark';
    } else {
      return 'light';
    }
  }
  return 'light';
}

// Change directly as soon as system mode is change only if theme is set to 'auto'
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function (e) {
    let currentTheme = localStorage.getItem('theme') || 'auto';
    if (currentTheme === 'auto') {
        document.documentElement.setAttribute('data-bs-theme', getSystemColorScheme());
    }
});

// Change on user action
document.addEventListener('DOMContentLoaded', (event) => {
    const htmlElement = document.documentElement;
    const lightIcon = document.getElementById('icon-light');
    const darkIcon = document.getElementById('icon-dark');
    const autoIcon = document.getElementById('icon-auto');

    // Set the default theme to dark if no setting is found in local storage
    let currentTheme = localStorage.getItem('theme') || 'auto';
    if (currentTheme === 'auto') {
        htmlElement.setAttribute('data-bs-theme', getSystemColorScheme());
        autoIcon.style.display = 'inline';
    } else {
        htmlElement.setAttribute('data-bs-theme', currentTheme);
        if (currentTheme === 'light') {
            lightIcon.style.display = 'inline';
        } else {
            darkIcon.style.display = 'inline';
        }
    }
    const selectedMode = document.getElementsByClassName(currentTheme)[0];
    selectedMode.classList.add("selected");

    const toDark = document.getElementById('id_dark_mode');
    toDark.addEventListener('click', function () {
        localStorage.setItem('theme', 'dark');
    });

    const toLight = document.getElementById('id_light_mode');
    toLight.addEventListener('click', function () {
        localStorage.setItem('theme', 'light');
    });

    const toAuto = document.getElementById('id_system_mode');
    toAuto.addEventListener('click', function () {
        localStorage.setItem('theme', 'auto');
    });
});