(() => {
  const STATE_KEY = "__mkdocsTranslateSwitchState";
  const SCRIPT_ID = "mkdocs-google-translate-script";
  const WRAPPER_ID = "mkdocs-lang-switch";
  const TRANSLATE_DIV_ID = "google_translate_element";
  const COOKIE_NAME = "googtrans";
  const COOKIE_FR = "/auto/fr";
  const COOKIE_EN = "/auto/en";
  const SCRIPT_SRC = "https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";

  function getCookie(name) {
    const prefix = `${name}=`;
    const parts = document.cookie ? document.cookie.split("; ") : [];
    for (const part of parts) {
      if (part.startsWith(prefix)) {
        return decodeURIComponent(part.slice(prefix.length));
      }
    }
    return "";
  }

  function setGoogtransCookie(value) {
    const encoded = encodeURIComponent(value);
    const oneYear = 60 * 60 * 24 * 365;
    document.cookie = `${COOKIE_NAME}=${encoded}; path=/; max-age=${oneYear}; SameSite=Lax`;
  }

  function getCurrentLang() {
    const value = getCookie(COOKIE_NAME).toLowerCase();
    return value.endsWith("/en") ? "en" : "fr";
  }

  function ensureHiddenTranslateDiv() {
    let node = document.getElementById(TRANSLATE_DIV_ID);
    if (!node) {
      node = document.createElement("div");
      node.id = TRANSLATE_DIV_ID;
      node.hidden = true;
      document.body.appendChild(node);
    }
    return node;
  }

  function ensureSwitch() {
    let wrapper = document.getElementById(WRAPPER_ID);
    if (!wrapper) {
      wrapper = document.createElement("div");
      wrapper.id = WRAPPER_ID;
      wrapper.setAttribute("role", "group");
      wrapper.setAttribute("aria-label", "Language switch");
      wrapper.innerHTML = [
        "<button type=\"button\" class=\"lang-btn\" data-lang=\"fr\" aria-pressed=\"false\">FR</button>",
        "<button type=\"button\" class=\"lang-btn\" data-lang=\"en\" aria-pressed=\"false\">EN</button>",
      ].join("");
      document.body.appendChild(wrapper);
    }
    return wrapper;
  }

  function updateGoogleCombo(lang) {
    const combo = document.querySelector(".goog-te-combo");
    if (!combo) {
      return false;
    }
    const target = lang === "en" ? "en" : "fr";
    if (combo.value !== target) {
      combo.value = target;
      combo.dispatchEvent(new Event("change", { bubbles: true }));
    }
    return true;
  }

  function refreshActive() {
    const wrapper = document.getElementById(WRAPPER_ID);
    if (!wrapper) {
      return;
    }
    const lang = getCurrentLang();
    const buttons = wrapper.querySelectorAll(".lang-btn");
    buttons.forEach((button) => {
      const active = button.getAttribute("data-lang") === lang;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  function applyLang(lang) {
    const cookieValue = lang === "en" ? COOKIE_EN : COOKIE_FR;
    setGoogtransCookie(cookieValue);
    refreshActive();
    if (!updateGoogleCombo(lang)) {
      window.location.reload();
    }
  }

  function bindSwitchHandler(wrapper) {
    if (wrapper.dataset.bound === "1") {
      return;
    }
    wrapper.dataset.bound = "1";
    wrapper.addEventListener("click", (event) => {
      const button = event.target.closest(".lang-btn");
      if (!button) {
        return;
      }
      const lang = button.getAttribute("data-lang");
      if (lang === "fr" || lang === "en") {
        applyLang(lang);
      }
    });
  }

  function ensureGoogleInitCallback() {
    if (window.__mkdocsGoogleTranslateInitBound) {
      return;
    }
    window.__mkdocsGoogleTranslateInitBound = true;

    window.googleTranslateElementInit = function googleTranslateElementInit() {
      if (
        window.__mkdocsGoogleTranslateElementCreated ||
        !window.google ||
        !window.google.translate ||
        !window.google.translate.TranslateElement
      ) {
        refreshActive();
        return;
      }

      window.__mkdocsGoogleTranslateElementCreated = true;
      new window.google.translate.TranslateElement(
        {
          pageLanguage: "fr",
          includedLanguages: "fr,en",
          autoDisplay: false,
        },
        TRANSLATE_DIV_ID
      );

      const lang = getCurrentLang();
      let tries = 0;
      const timer = window.setInterval(() => {
        tries += 1;
        if (updateGoogleCombo(lang) || tries > 20) {
          window.clearInterval(timer);
          refreshActive();
        }
      }, 100);
    };
  }

  function ensureGoogleScript() {
    if (document.getElementById(SCRIPT_ID)) {
      return;
    }

    const existing = document.querySelector(`script[src=\"${SCRIPT_SRC}\"]`);
    if (existing) {
      existing.id = SCRIPT_ID;
      return;
    }

    const script = document.createElement("script");
    script.id = SCRIPT_ID;
    script.src = SCRIPT_SRC;
    script.async = true;
    document.head.appendChild(script);
  }

  function init() {
    ensureHiddenTranslateDiv();
    const wrapper = ensureSwitch();
    bindSwitchHandler(wrapper);

    if (!getCookie(COOKIE_NAME)) {
      setGoogtransCookie(COOKIE_FR);
    }

    refreshActive();
    ensureGoogleInitCallback();
    ensureGoogleScript();

    if (window.google && window.google.translate && window.google.translate.TranslateElement) {
      window.googleTranslateElementInit();
    }
  }

  if (window[STATE_KEY]) {
    window[STATE_KEY].refreshActive();
    return;
  }

  window[STATE_KEY] = { refreshActive };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
