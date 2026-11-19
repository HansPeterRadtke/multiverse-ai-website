/* Shared navigation and a contact form that prepares a local email draft only. */
(() => {
  const menu = document.querySelector('.mobile-toggle');
  const mobileNav = document.querySelector('.mobile-nav');
  if (menu && mobileNav) {
    menu.addEventListener('click', () => {
      const opening = menu.getAttribute('aria-expanded') !== 'true';
      menu.setAttribute('aria-expanded', String(opening));
      mobileNav.classList.toggle('open', opening);
    });
  }

  const form = document.getElementById('inquiry-form');
  if (!form) return;

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    const values = new FormData(form);
    const get = (field, limit) => String(values.get(field) || '').trim().slice(0, limit);
    const name = get('name', 120);
    const email = get('email', 200);
    const company = get('company', 160);
    const problem = get('problem', 2100);
    const systems = get('systems', 260);

    const subject = 'Multiverse technology inquiry' + (company ? ' — ' + company : '');
    const lines = [
      'Contact name: ' + name,
      'Reply address: ' + email,
      ...(company ? ['Organization: ' + company] : []),
      '',
      'Current problem and desired result:',
      problem,
      ...(systems ? ['', 'Relevant software or systems: ' + systems] : []),
      '',
      'Prepared from the Multiverse website. Please review before sending.'
    ];
    const uri = 'mailto:multiverse3dhpr@gmail.com?subject=' +
      encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
    const status = document.getElementById('form-status');
    if (status) status.textContent =
      'Your email application should open with a draft. Review it and choose Send there. If it does not open, use the direct email link on this page.';
    // This navigation opens a mail application; it does not transmit the form
    // to the website, store it in browser storage, or confirm the message was sent.
    window.location.href = uri;
  });
})();
