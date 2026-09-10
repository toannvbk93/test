import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CorporateSiteTest(unittest.TestCase):
    def html_files(self):
        return sorted(ROOT.glob("*.html"))

    def test_pages_exist(self):
        names = {p.name for p in self.html_files()}
        for required in ("index.html", "jobs.html", "contact.html", "company.html"):
            self.assertIn(required, names)

    def test_no_ga4_on_corporate_site(self):
        for path in self.html_files():
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("G-6G2V112D2X", text, path.name)
            self.assertNotIn("googletagmanager.com/gtag", text, path.name)

    def test_nav_includes_local_jobs_page(self):
        for path in self.html_files():
            text = path.read_text(encoding="utf-8")
            self.assertIn('href="jobs.html"', text, path.name)
            self.assertIn("js/i18n.js", text, path.name)
            self.assertIn('data-lang="ja"', text, path.name)
            self.assertIn('data-lang="vi"', text, path.name)

    def test_jobs_page_points_at_jobs_host(self):
        text = (ROOT / "jobs.html").read_text(encoding="utf-8")
        self.assertIn("jobs.kataosogo.jp", text)
        self.assertIn('data-i18n="jobs.siteTitle"', text)

    def test_pages_have_charset(self):
        for path in self.html_files():
            text = path.read_text(encoding="utf-8")
            self.assertIn("charset", text.lower(), path.name)


if __name__ == "__main__":
    unittest.main()
