#!/usr/bin/env python3
"""Generate all static HTML pages for a kataosogo.jp clone."""

from pathlib import Path
from textwrap import dedent

OUT_DIR = Path(__file__).resolve().parent

NAV_ITEMS = [
    ("index.html", "ホーム"),
    ("company.html", "会社概要"),
    ("greeting.html", "代表者挨拶"),
    ("business.html", "事業内容"),
    ("it-services.html", "ITサービス"),
    ("for-companies.html", "企業様へ"),
    ("recruitment.html", "採用情報"),
    ("jobs.html", "求人情報"),
    ("news.html", "ニュース"),
]

IT_SERVICE_PAGES = {
    "it-services.html",
    "offshore-development.html",
    "application-development.html",
    "migration.html",
    "maintenance-operations.html",
    "cloud-computing.html",
    "ai-genai.html",
    "erp-crm.html",
    "cyber-security.html",
}

IT_SERVICES = [
    {
        "slug": "offshore-development",
        "num": "01",
        "title": "オフショア開発",
        "en": "Offshore Development",
        "summary": "ベトナムの優秀なITエンジニアと日本企業をつなぎ、日本品質×合理コストの開発を実現",
        "image": "photo-team.jpg",
        "lead": "ベトナム拠点のエンジニアリング力と、日本側のブリッジ体制を組み合わせ、要件定義からリリース・保守まで一貫して対応します。コミュニケーションロスを抑えつつ、開発スピードとコスト効率を両立します。",
        "features": [
            ("ブリッジSE体制", "日本語・ベトナム語・英語での円滑なコミュニケーションと進捗管理"),
            ("ラボ型／請負型", "専属チームによるラボ開発、または要件固定の請負開発に対応"),
            ("日本品質の工程管理", "設計レビュー・コードレビュー・テスト・納品基準を日本基準で運用"),
            ("柔軟なスケール", "プロジェクト規模に応じてチーム規模を拡大・縮小可能"),
        ],
        "process": [
            ("ヒアリング", "課題・予算・スケジュールの整理"),
            ("提案・見積", "体制・技術・コストのご提案"),
            ("キックオフ", "チーム編成と開発ルールの合意"),
            ("開発・検証", "アジャイル／ウォーターフォール対応"),
            ("納品・運用", "移行支援と継続改善"),
        ],
        "benefits": [
            "優秀なベトナムIT人材を、日本品質の管理体制で活用",
            "国内開発と比べてコストを抑えつつスピードを確保",
            "要件の曖昧さにも対応できるブリッジSEサポート",
        ],
    },
    {
        "slug": "application-development",
        "num": "02",
        "title": "アプリケーション開発",
        "en": "Application Development",
        "summary": "Web・モバイル・業務システムなど、ビジネス要件に最適化したアプリ開発",
        "image": "photo-office.jpg",
        "lead": "新規サービス立ち上げから既存システムの刷新まで、企画・設計・実装・テスト・リリースをワンストップで支援します。モダンな技術スタックと堅実な品質管理で、使いやすく保守しやすいアプリケーションを構築します。",
        "features": [
            ("Webアプリケーション", "業務ポータル、SaaS、社内システム、API連携など"),
            ("モバイルアプリ", "iOS / Android（ネイティブ・クロスプラットフォーム）"),
            ("業務システム", "受発注・在庫・勤怠・顧客管理などのカスタム開発"),
            ("UI/UX設計", "現場の業務フローに沿った画面設計と操作性の最適化"),
        ],
        "process": [
            ("要件定義", "業務課題と機能要件の明確化"),
            ("設計", "アーキテクチャ・画面・データ設計"),
            ("実装", "アジャイル開発と定期デモ"),
            ("テスト", "単体・結合・受け入れ試験"),
            ("リリース", "本番展開と初期サポート"),
        ],
        "benefits": [
            "ビジネス目標に直結する機能設計",
            "将来の拡張・保守を見据えたアーキテクチャ",
            "オフショア体制によるコスト効率の高い開発",
        ],
    },
    {
        "slug": "migration",
        "num": "03",
        "title": "移行",
        "en": "System Migration",
        "summary": "レガシーシステムからクラウド／新基盤への安全・確実な移行支援",
        "image": "photo-network.jpg",
        "lead": "古い基幹システムやオンプレミス環境の刷新、クラウド移行、データ移行まで、ダウンタイムとリスクを最小化しながら段階的に進めます。現状分析から移行計画、リハーサル、本番切替、安定化まで一貫して伴走します。",
        "features": [
            ("レガシー刷新", "老朽化した業務システム・基幹系の再構築／リライト"),
            ("クラウド移行", "オンプレミスからAWS／Azure／GCP等への移行"),
            ("データ移行", "データクレンジング、マッピング、検証、切替計画"),
            ("並行稼働支援", "段階移行・ロールバック設計によるリスク低減"),
        ],
        "process": [
            ("現状分析", "資産・依存関係・リスクの棚卸し"),
            ("移行計画", "方式・スケジュール・切替戦略の策定"),
            ("構築・検証", "新環境構築と移行リハーサル"),
            ("本番切替", "計画的なカットオーバー"),
            ("安定化", "監視・障害対応・最適化"),
        ],
        "benefits": [
            "移行リスクと業務停止時間の最小化",
            "将来の運用コスト削減と拡張性の向上",
            "技術負債の解消とセキュリティ強化",
        ],
    },
    {
        "slug": "maintenance-operations",
        "num": "04",
        "title": "保守＆運用支援",
        "en": "Maintenance & Operations",
        "summary": "システムの安定稼働を支える、監視・障害対応・改善の継続サポート",
        "image": "photo-business.jpg",
        "lead": "開発後も安心してご利用いただけるよう、障害対応、定期メンテナンス、性能改善、小規模改修まで運用チームが継続支援します。SLAに応じた対応体制で、ビジネスの止まらないIT基盤を維持します。",
        "features": [
            ("監視・アラート", "可用性・性能・エラーの常時監視と一次対応"),
            ("障害対応", "原因調査、応急措置、恒久対策まで迅速に対応"),
            ("定期保守", "パッチ適用、バックアップ確認、脆弱性対応"),
            ("改善・改修", "運用改善提案と小規模機能追加"),
        ],
        "process": [
            ("引き継ぎ", "システム構成・運用手順の把握"),
            ("体制設計", "窓口・SLA・エスカレーションの定義"),
            ("運用開始", "監視・問い合わせ対応の開始"),
            ("定期報告", "稼働状況と改善提案の共有"),
            ("継続改善", "コスト最適化と品質向上"),
        ],
        "benefits": [
            "社内ITリソースの負荷軽減",
            "障害時の迅速な復旧と再発防止",
            "運用データを活かした継続的な改善",
        ],
    },
    {
        "slug": "cloud-computing",
        "num": "05",
        "title": "クラウドコンピューティング",
        "en": "Cloud Computing",
        "summary": "設計・構築・最適化まで、クラウド活用をトータルで支援",
        "image": "photo-office.jpg",
        "lead": "クラウドの導入検討からアーキテクチャ設計、構築、コスト最適化、運用までを支援します。セキュリティと可用性を両立したクラウド基盤で、スケーラブルなビジネス成長を支えます。",
        "features": [
            ("クラウド設計・構築", "AWS / Azure / GCP を活用した基盤構築"),
            ("コンテナ／サーバレス", "Docker、Kubernetes、Functions 等の活用"),
            ("コスト最適化", "利用状況分析とリソース最適化"),
            ("セキュリティ設計", "IAM、ネットワーク、暗号化、監査ログの整備"),
        ],
        "process": [
            ("アセスメント", "現状課題とクラウド適合性の評価"),
            ("設計", "構成・セキュリティ・コスト設計"),
            ("構築", "インフラ／アプリ基盤の実装"),
            ("移行・展開", "段階的な本番展開"),
            ("運用最適化", "監視・FinOps・改善"),
        ],
        "benefits": [
            "初期投資を抑えつつ迅速にスケール可能",
            "可用性と災害対策の強化",
            "運用自動化による人的負荷の削減",
        ],
    },
    {
        "slug": "ai-genai",
        "num": "06",
        "title": "AI / Gen AI",
        "en": "AI & Generative AI",
        "summary": "業務効率化・顧客体験向上に繋がるAI／生成AIソリューションの導入支援",
        "image": "photo-meeting.jpg",
        "lead": "チャットボット、文書要約、画像認識、需要予測など、生成AI・機械学習を実務に落とし込みます。PoCから本番導入、ガバナンス整備まで、安全かつ効果的なAI活用を支援します。",
        "features": [
            ("生成AI活用", "社内FAQ、文書作成支援、ナレッジ検索、業務自動化"),
            ("機械学習", "予測・分類・レコメンドなどのモデル構築"),
            ("LLM連携開発", "API連携、RAG、社内データとの安全な接続"),
            ("AIガバナンス", "セキュリティ、個人情報、利用ポリシーの整備"),
        ],
        "process": [
            ("ユースケース選定", "効果と実現性の高い課題の特定"),
            ("PoC", "小規模検証で効果を確認"),
            ("本開発", "本番品質のシステム化"),
            ("導入・教育", "現場展開と運用ルール整備"),
            ("効果測定", "KPIモニタリングと改善"),
        ],
        "benefits": [
            "定型業務の自動化と生産性向上",
            "顧客対応品質・スピードの改善",
            "データに基づく意思決定の高度化",
        ],
    },
    {
        "slug": "erp-crm",
        "num": "07",
        "title": "ERP - CRM",
        "en": "ERP & CRM",
        "summary": "基幹業務と顧客管理を統合し、経営の可視化と営業生産性を向上",
        "image": "photo-workplace.jpg",
        "lead": "ERP／CRMの導入・カスタマイズ・周辺連携・データ移行までを支援します。部門ごとに分断された業務データを統合し、経営判断と現場オペレーションの両方を強化します。",
        "features": [
            ("ERP導入・連携", "会計・販売・在庫・生産など基幹業務の統合"),
            ("CRM構築", "顧客管理、商談管理、マーケティング自動化"),
            ("カスタマイズ", "業種・業務フローに合わせた機能拡張"),
            ("データ連携", "既存システム・EC・BIとのシームレス連携"),
        ],
        "process": [
            ("業務分析", "現行フローと課題の可視化"),
            ("要件定義", "標準機能とカスタム範囲の整理"),
            ("構築・移行", "設定、開発、データ移行"),
            ("トレーニング", "現場への定着支援"),
            ("運用改善", "活用度向上と追加改善"),
        ],
        "benefits": [
            "経営データのリアルタイム可視化",
            "部門横断の業務効率化",
            "顧客対応力と売上機会の最大化",
        ],
    },
    {
        "slug": "cyber-security",
        "num": "08",
        "title": "サイバー・セキュリティ",
        "en": "Cyber Security",
        "summary": "脅威から情報資産を守る、診断・対策・運用のセキュリティ支援",
        "image": "photo-network.jpg",
        "lead": "脆弱性診断、セキュリティ設計、監視、インシデント対応まで、多層防御の考え方で情報資産を保護します。開発段階からのセキュア設計と、運用フェーズの継続的な対策を両立します。",
        "features": [
            ("脆弱性診断", "Webアプリ・インフラ・クラウドのセキュリティ診断"),
            ("セキュア開発", "設計・実装段階でのセキュリティ要件組み込み"),
            ("監視・防御", "ログ監視、不正検知、アクセス制御の強化"),
            ("インシデント対応", "初動対応、原因分析、再発防止策の策定"),
        ],
        "process": [
            ("現状評価", "リスクと対策状況のアセスメント"),
            ("対策設計", "優先度に基づく改善ロードマップ"),
            ("実装", "技術対策・運用ルールの導入"),
            ("検証", "診断・ペネトレーションテスト"),
            ("継続運用", "監視・教育・定期見直し"),
        ],
        "benefits": [
            "情報漏洩・サービス停止リスクの低減",
            "取引先・顧客からの信頼向上",
            "コンプライアンス要件への対応強化",
        ],
    },
]


def build_nav_links(active_file: str) -> tuple[str, str]:
    """Build main nav links and contact CTA (single contact entry)."""
    nav_parts = []
    for href, label in NAV_ITEMS:
        if href == "it-services.html":
            is_active = active_file in IT_SERVICE_PAGES
        else:
            is_active = href == active_file
        active_attr = " class='active'" if is_active else ""
        nav_parts.append(f'          <li><a href="{href}"{active_attr}>{label}</a></li>')
    nav_links = "\n".join(nav_parts)
    cta_active = " active" if active_file == "contact.html" else ""
    nav_cta = f'                  <li class="nav-cta"><a href="contact.html" class="btn-nav{cta_active}">お問い合わせ</a></li>'
    return nav_links, nav_cta

FOOTER_HTML = dedent(
    """\
    <footer class="site-footer">
      <div class="container footer-grid">
        <div class="footer-brand">
          <img src="images/logo.png" alt="KATAO" class="footer-logo">
          <p><strong>株式会社カタオ総合</strong></p>
          <p class="footer-tagline">機会を繋ぐ・未来を築く</p>
        </div>
        <div class="footer-col">
          <h4>会社情報</h4>
          <ul>
            <li><a href="company.html">会社概要</a></li>
            <li><a href="greeting.html">代表者挨拶</a></li>
            <li><a href="business.html">事業内容</a></li>
            <li><a href="news.html">ニュース</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>サービス</h4>
          <ul>
            <li><a href="it-services.html">ITアウトソーシング</a></li>
            <li><a href="offshore-development.html">オフショア開発</a></li>
            <li><a href="for-companies.html">企業様へ</a></li>
            <li><a href="contact.html">お問い合わせ</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>お問い合わせ</h4>
          <address>〒123-0861<br>東京都足立区加賀１－７－５</address>
          <p>TEL: <a href="tel:0363362753">03-6336-2753</a></p>
          <p>Email: <a href="mailto:kataosogo.info@gmail.com">kataosogo.info@gmail.com</a></p>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="container">
          <p>© 2026 株式会社カタオ総合 All Rights Reserved.</p>
        </div>
      </div>
    </footer>
    """
)


def shell(title: str, active_file: str, body_html: str, hero_html: str = "") -> str:
    """Wrap a page body with shared header/nav/footer shell."""
    nav_links, nav_cta = build_nav_links(active_file)
    hero = f"\n{hero_html}\n" if hero_html else "\n"

    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="ja">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>{title} | 株式会社カタオ総合</title>
          <link rel="stylesheet" href="css/style.css">
        </head>
        <body>
          <div class="page-loader">
            <div class="loader-spinner"></div>
            <img src="images/logo.png" alt="" class="loader-logo">
            <div class="loader-bar"><div class="loader-bar-fill"></div></div>
            <p class="loader-text">読み込み中...</p>
          </div>
          <div class="page-transition"></div>
          <div class="scroll-progress"></div>

          <header class="site-header">
            <div class="container header-inner">
              <a class="logo-link" href="index.html">
                <img src="images/logo.png" alt="株式会社カタオ総合 ロゴ">
                <span>株式会社カタオ総合</span>
              </a>
              <button class="nav-toggle" aria-label="メニュー">☰</button>
              <nav class="main-nav" aria-label="メインナビゲーション">
                <ul>
        {nav_links}
        {nav_cta}
                </ul>
              </nav>
            </div>
          </header>{hero}
          <main class="site-main">
            <div class="container">
        {body_html}
            </div>
          </main>
        {FOOTER_HTML}
          <button class="back-to-top" aria-label="トップへ戻る">↑</button>
          <script src="js/main.js"></script>
        </body>
        </html>
        """
    )


def page_hero(title: str, subtitle: str = "") -> str:
    sub = f"<p>{subtitle}</p>" if subtitle else ""
    return dedent(f"""\
    <section class="hero hero--compact">
      <div class="hero-overlay"></div>
      <div class="hero-content reveal">
        <h1>{title}</h1>
        {sub}
      </div>
    </section>
    """)


def write_page(filename: str, title: str, active_file: str, body_html: str, hero_html: str = "") -> None:
    """Write a complete HTML page."""
    page = shell(title, active_file, dedent(body_html).strip(), dedent(hero_html).strip())
    (OUT_DIR / filename).write_text(page, encoding="utf-8")
    print(f"  ✓ {filename}")


def shell_home(title: str, body_html: str, hero_html: str) -> str:
    """Homepage shell — full-width sections, no container wrapper on main."""
    nav_links, nav_cta = build_nav_links("index.html")

    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="ja">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta name="description" content="株式会社カタオ総合 — ベトナムと日本をつなぐ外国人人材紹介・登録支援機関">
          <title>{title} | 株式会社カタオ総合</title>
          <link rel="stylesheet" href="css/style.css">
        </head>
        <body>
          <div class="page-loader">
            <div class="loader-spinner"></div>
            <img src="images/logo.png" alt="" class="loader-logo">
            <div class="loader-bar"><div class="loader-bar-fill"></div></div>
            <p class="loader-text">読み込み中...</p>
          </div>
          <div class="page-transition"></div>
          <div class="scroll-progress"></div>

          <header class="site-header">
            <div class="container header-inner">
              <a class="logo-link" href="index.html">
                <img src="images/logo.png" alt="株式会社カタオ総合 ロゴ">
                <span>株式会社カタオ総合</span>
              </a>
              <button class="nav-toggle" aria-label="メニュー">☰</button>
              <nav class="main-nav" aria-label="メインナビゲーション">
                <ul>
        {nav_links}
        {nav_cta}
                </ul>
              </nav>
            </div>
          </header>
        {hero_html}
          <main class="site-main site-main--home">
        {body_html}
          </main>
        {FOOTER_HTML}
          <button class="back-to-top" aria-label="トップへ戻る">↑</button>
          <script src="js/main.js"></script>
        </body>
        </html>
        """
    )


def write_home(body_html: str, hero_html: str) -> None:
    page = shell_home("ホーム", dedent(body_html).strip(), dedent(hero_html).strip())
    (OUT_DIR / "index.html").write_text(page, encoding="utf-8")
    print("  ✓ index.html")


def shell_fullwidth(title: str, active_file: str, content_html: str) -> str:
    """Full-width page shell — hero and sections without container wrapper."""
    nav_links, nav_cta = build_nav_links(active_file)

    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="ja">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>{title} | 株式会社カタオ総合</title>
          <link rel="stylesheet" href="css/style.css">
        </head>
        <body>
          <div class="page-loader">
            <div class="loader-spinner"></div>
            <img src="images/logo.png" alt="" class="loader-logo">
            <div class="loader-bar"><div class="loader-bar-fill"></div></div>
            <p class="loader-text">読み込み中...</p>
          </div>
          <div class="page-transition"></div>
          <div class="scroll-progress"></div>

          <header class="site-header">
            <div class="container header-inner">
              <a class="logo-link" href="index.html">
                <img src="images/logo.png" alt="株式会社カタオ総合 ロゴ">
                <span>株式会社カタオ総合</span>
              </a>
              <button class="nav-toggle" aria-label="メニュー">☰</button>
              <nav class="main-nav" aria-label="メインナビゲーション">
                <ul>
        {nav_links}
        {nav_cta}
                </ul>
              </nav>
            </div>
          </header>
        {content_html}
        {FOOTER_HTML}
          <button class="back-to-top" aria-label="トップへ戻る">↑</button>
          <script src="js/main.js"></script>
        </body>
        </html>
        """
    )


def write_fullwidth_page(filename: str, title: str, active_file: str, content_html: str) -> None:
    page = shell_fullwidth(title, active_file, dedent(content_html).strip())
    (OUT_DIR / filename).write_text(page, encoding="utf-8")
    print(f"  ✓ {filename}")


def build_home() -> None:
    hero_html = """
    <section class="hero hero--home">
      <img src="images/photo-office.jpg" alt="日本・ベトナムをつなぐ架け橋" class="hero-image">
      <div class="hero-overlay"></div>
      <div class="hero-content reveal">
        <span class="hero-badge">外国人人材紹介事業</span>
        <h1>機会を繋ぐ・未来を築く</h1>
        <p>ベトナムと日本をつなぐ信頼のパートナー — 人材紹介から定着支援までワンストップ</p>
        <div class="hero-actions">
          <a href="for-companies.html" class="btn btn-primary">企業様はこちら</a>
          <a href="contact.html" class="btn btn-outline">お問い合わせ</a>
        </div>
      </div>
    </section>
    """
    body_html = """
    <!-- About -->
    <section class="section-block section-about">
      <div class="container about-split">
        <div class="about-text reveal-left">
          <span class="section-label">About Us</span>
          <h2>日本とベトナムをつなぐ<br>総合人材サービス</h2>
          <p>株式会社カタオ総合は、革新的なソリューションを提供し、お客様の信頼に応えることを使命としています。ベトナムをはじめとする海外の教育機関・団体との強固なネットワークを活かし、日本語能力・専門スキル・勤労意識に優れた人材を厳選・育成し、日本企業へ紹介しております。</p>
          <p>「信頼」「誠実」「挑戦」を企業理念とし、社会に貢献できる企業であり続けます。</p>
          <a href="company.html" class="btn btn-primary">会社概要を見る</a>
        </div>
        <div class="about-image reveal-right">
          <img src="images/photo-network.jpg" alt="国際人材紹介サービス">
        </div>
      </div>
    </section>

    <!-- Stats -->
    <section class="section-block section-stats">
      <div class="container stats-bar">
        <div class="stat reveal" data-delay="1"><span class="stat-num">2023</span><span class="stat-label">設立年</span></div>
        <div class="stat reveal" data-delay="2"><span class="stat-num">16</span><span class="stat-label">特定技能業種</span></div>
        <div class="stat reveal" data-delay="3"><span class="stat-num">7+</span><span class="stat-label">事業分野</span></div>
        <div class="stat reveal" data-delay="4"><span class="stat-num">100%</span><span class="stat-label">ワンストップ支援</span></div>
      </div>
    </section>

    <!-- Services -->
    <section class="section-block section-services">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-label">Services</span>
          <h2>事業内容</h2>
          <p>人材紹介から生活支援、教育コンサルティングまで幅広く対応</p>
        </div>
        <div class="services-grid">
          <a href="business.html" class="service-card reveal" data-delay="1">
            <img src="images/photo-workplace.jpg" alt="技能実習・特定技能">
            <div class="service-card-body">
              <h3>技能実習・特定技能</h3>
              <p>育成・送出し、16業種対応の登録支援機関サービス</p>
            </div>
          </a>
          <a href="business.html" class="service-card reveal" data-delay="2">
            <img src="images/photo-team.jpg" alt="高度人材紹介">
            <div class="service-card-body">
              <h3>高度人材紹介</h3>
              <p>技術・人文知識・国際業務ビザ対応</p>
            </div>
          </a>
          <a href="business.html" class="service-card reveal" data-delay="3">
            <img src="images/photo-business.jpg" alt="生活・就業支援">
            <div class="service-card-body">
              <h3>生活・就業支援</h3>
              <p>ビザ、住居、日本語、定着支援のトータルサポート</p>
            </div>
          </a>
          <a href="business.html" class="service-card reveal" data-delay="4">
            <img src="images/photo-meeting.jpg" alt="通訳・翻訳・研修">
            <div class="service-card-body">
              <h3>通訳・翻訳・研修</h3>
              <p>言語サービスと教育コンサルティング</p>
            </div>
          </a>
          <a href="business.html" class="service-card reveal" data-delay="5">
            <img src="images/photo-network.jpg" alt="日越連携支援">
            <div class="service-card-body">
              <h3>日越連携支援</h3>
              <p>技術協力・投資・生産分野の国際連携</p>
            </div>
          </a>
          <a href="it-services.html" class="service-card reveal" data-delay="6">
            <img src="images/photo-office.jpg" alt="オフショア開発・ITアウトソーシング">
            <div class="service-card-body">
              <h3>ITアウトソーシング</h3>
              <p>オフショア開発、アプリ開発、クラウド、AI、セキュリティなど</p>
            </div>
          </a>
        </div>
        <div class="section-cta reveal">
          <a href="business.html" class="btn btn-primary">事業内容の詳細を見る</a>
        </div>
      </div>
    </section>

    <!-- Why Us -->
    <section class="section-block section-why">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-label">Why KATAO</span>
          <h2>カタオ総合が選ばれる理由</h2>
        </div>
        <div class="why-grid">
          <div class="why-card reveal" data-delay="1">
            <div class="why-icon">01</div>
            <h3>ワンストップ対応</h3>
            <p>人材選定から採用、入国後の生活・職場定着支援まで一貫したサービス</p>
          </div>
          <div class="why-card reveal" data-delay="2">
            <div class="why-icon">02</div>
            <h3>ベトナム語サポート</h3>
            <p>面接・生活指導・日常相談すべてベトナム語で対応可能</p>
          </div>
          <div class="why-card reveal" data-delay="3">
            <div class="why-icon">03</div>
            <h3>法的手続き代行</h3>
            <p>在留資格、ビザ発給、入国サポートまで全て代行</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Process -->
    <section class="section-block section-process">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-label">Process</span>
          <h2>採用の流れ</h2>
          <p>人材募集から就業開始まで5ステップで完全サポート</p>
        </div>
        <div class="steps">
          <div class="step reveal" data-delay="1"><div class="step-num">1</div><h4>人材募集・紹介</h4><p>ご要望をお伺いし最適な人材をご提案</p></div>
          <div class="step reveal" data-delay="2"><div class="step-num">2</div><h4>面接対応</h4><p>母国語スタッフが同行サポート</p></div>
          <div class="step reveal" data-delay="3"><div class="step-num">3</div><h4>内定・書類申請</h4><p>ビザ申請などトータルサポート</p></div>
          <div class="step reveal" data-delay="4"><div class="step-num">4</div><h4>入国準備</h4><p>生活環境整備を万全に</p></div>
          <div class="step reveal" data-delay="5"><div class="step-num">5</div><h4>就業開始</h4><p>定期的フォローアップ</p></div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="section-block section-cta-banner">
      <div class="container cta-inner reveal">
        <h2>まずはお気軽にご相談ください</h2>
        <p>貴社の人材課題に最適なソリューションをご提案いたします</p>
        <div class="hero-actions">
          <a href="contact.html" class="btn btn-white">お問い合わせ</a>
          <a href="for-companies.html" class="btn btn-outline-white">企業様向け情報</a>
        </div>
      </div>
    </section>
    """
    write_home(body_html, hero_html)


def build_company() -> None:
    body_html = """
    <article>
      <table class="info-table">
        <tbody>
          <tr><th scope="row">会社名</th><td>株式会社カタオ総合</td></tr>
          <tr><th scope="row">本社所在地</th><td>〒123-0861 東京都足立区加賀１－７－５</td></tr>
          <tr><th scope="row">電話番号</th><td>03-6336-2753</td></tr>
          <tr><th scope="row">メールアドレス</th><td><a href="mailto:kataosogo.info@gmail.com">kataosogo.info@gmail.com</a></td></tr>
          <tr><th scope="row">ホームページ</th><td><a href="https://kataosogo.jp/">https://kataosogo.jp</a></td></tr>
          <tr><th scope="row">設立年月日</th><td>2023年6月1日</td></tr>
          <tr><th scope="row">資本金</th><td>6,500,000円</td></tr>
          <tr><th scope="row">代表取締役</th><td>ファム・バン・カン</td></tr>
          <tr><th scope="row">職業紹介 許可番号</th><td>13-ユ-315921</td></tr>
          <tr><th scope="row">登録支援機関許可番号</th><td>25登-012387</td></tr>
        </tbody>
      </table>
    </article>

    <section class="section">
      <div class="mission-block">
      <h2>使命（Mission）</h2>
      <p>ベトナムと日本をつなぐ架け橋として、人と企業、技術と文化を結び、双方の持続的な発展に貢献します。</p>
      </div>
    </section>

    <section class="section">
      <div class="mission-block">
      <h2>ビジョン（Vision）</h2>
      <p>信頼される国際パートナーとして、人材・貿易・教育の分野でアジアを代表する企業を目指します。</p>
      </div>
    </section>

    <section class="section">
      <div class="mission-block">
      <h2>企業方針（Policy）</h2>
      <p>誠実（Seijitsu）・信頼（Shinrai）・挑戦（Chousen）＝ 真心をもって信頼を築き、常に新たな挑戦を続ける。</p>
      </div>
    </section>

    <section class="section">
      <div class="mission-block">
      <h2>スローガン（Slogan）</h2>
      <p>人と企業をつなぎ、未来を創る。Connecting People and Companies, Creating the Future.</p>
      </div>
    </section>
    """
    write_page("company.html", "会社概要", "company.html", body_html, page_hero("会社概要", "Company Profile"))


def build_greeting() -> None:
    body_html = """
    <article class="greeting-article">
      <div class="greeting-profile reveal">
        <img src="images/photo-hero.jpg" alt="代表取締役 ファム・バン・カン">
        <p class="greeting-name">代表取締役　ファム・バン・カン</p>
      </div>
      <div class="greeting-text">
      <p>はじめに、株式会社カタオ総合を代表いたしまして、お客様ならびにビジネスパートナーの皆様のご健康とご繁栄を心よりお祈り申し上げます。平素より格別のご高配を賜り、厚く御礼申し上げます。</p>
      <p>私はベトナムの建設大学（National University of Civil Engineering）を卒業後、約20年間にわたり日本で勤務し、建設業界を中心に幅広い経験を積んでまいりました。その中で、日本の高度な技術力と誠実な企業文化を学び、「日本とベトナムをつなぐ架け橋となりたい」という強い想いを抱くようになりました。</p>
      <p>現在、日本では少子高齢化が進み、若年層の人材不足が深刻な課題となっております。一方で、ベトナムには優秀で勤勉、かつ学ぶ意欲にあふれた若者が数多く存在します。こうした人材が日本で働き、技術や経験を学ぶことは、両国の発展と相互理解の促進につながるものと確信しております。</p>
      <p>この理念のもと、株式会社カタオ総合は、貿易・観光・投資、そして特に人材交流の分野において、日本とベトナムを結ぶ信頼のパートナーとして設立されました。「最高のサービスでお客様の信頼に応えること」を企業方針に掲げ、誠実・信頼・挑戦の精神で事業を展開してまいります。</p>
      <p>今後ともご指導ご鞭撻を賜りますようお願い申し上げます。皆様の変わらぬご支援とご愛顧を心よりお願い申し上げます。</p>
      </div>
    </article>
    """
    write_page("greeting.html", "代表者挨拶", "greeting.html", body_html, page_hero("代表者挨拶"))


def build_business() -> None:
    content_html = """<section class="hero hero--business">
  <img src="images/photo-office.jpg" alt="事業内容" class="hero-image">
  <div class="hero-overlay"></div>
  <div class="hero-content reveal">
    <span class="hero-badge">Business Fields</span>
    <h1>事業内容</h1>
    <p>人材紹介からオフショア開発まで、ワンストップでサポート</p>
  </div>
</section>

<main class="site-main site-main--business">

  <section class="section-block section-about">
    <div class="container about-split">
      <div class="about-text reveal-left">
        <span class="section-label">Overview</span>
        <h2>国際人材紹介事業の概要</h2>
        <p>当社は、日本国内の多様化する企業ニーズに応えるため、海外人材の紹介およびマッチング事業を展開しております。</p>
        <p>ベトナムをはじめとする海外の教育機関や団体との強固なネットワークを活かし、日本語能力・専門スキル・勤労意識に優れた人材を厳選・育成し、日本企業へ紹介しています。</p>
        <p>また、企業様の受入れに関する法的手続きの支援、人材管理、生活サポートなど、採用後のフォロー体制も充実させ、企業と人材双方の信頼関係構築に努めております。</p>
      </div>
      <div class="about-image reveal-right">
        <img src="images/photo-network.jpg" alt="国際人材紹介ネットワーク">
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="biz-split">
        <div class="biz-image reveal-left">
          <img src="images/photo-meeting.jpg" alt="国際人材支援">
        </div>
        <div class="biz-content reveal-right">
          <span class="section-label">Support</span>
          <h2>国際人材の支援事業について</h2>
          <p>当社は、外国人材が日本で安心して働き、生活できるよう、入国前から就労後まで一貫したサポート体制を提供しております。</p>
          <div class="biz-support-grid">
            <div class="biz-support-item reveal" data-delay="1">
              <span class="biz-support-icon">01</span>
              <p>在留資格・ビザ申請、入国に関する手続き支援</p>
            </div>
            <div class="biz-support-item reveal" data-delay="2">
              <span class="biz-support-icon">02</span>
              <p>生活支援（住居・日本語学習・地域交流など）</p>
            </div>
            <div class="biz-support-item reveal" data-delay="3">
              <span class="biz-support-icon">03</span>
              <p>キャリア相談・職場定着・スキルアップ支援</p>
            </div>
            <div class="biz-support-item reveal" data-delay="4">
              <span class="biz-support-icon">04</span>
              <p>受入企業への管理・教育・文化理解のサポート</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Business Fields</span>
        <h2>業務分野</h2>
        <p>7つの事業分野で、企業と人材の双方をトータルサポート</p>
      </div>
      <div class="biz-field-grid">
        <a href="#field-1" class="biz-field-card reveal" data-delay="1">
          <img src="images/photo-workplace.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">01</span><h3>技能実習生・特定技能者の育成・送出し</h3></div>
        </a>
        <a href="#field-2" class="biz-field-card reveal" data-delay="2">
          <img src="images/photo-team.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">02</span><h3>日本企業への人材紹介</h3></div>
        </a>
        <a href="#field-3" class="biz-field-card reveal" data-delay="3">
          <img src="images/photo-business.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">03</span><h3>登録支援機関サービス</h3></div>
        </a>
        <a href="#field-4" class="biz-field-card reveal" data-delay="4">
          <img src="images/photo-meeting.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">04</span><h3>通訳・翻訳・研修・教育コンサル</h3></div>
        </a>
        <a href="#field-5" class="biz-field-card reveal" data-delay="5">
          <img src="images/photo-network.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">05</span><h3>国際連携・技術協力支援</h3></div>
        </a>
        <a href="#field-6" class="biz-field-card reveal" data-delay="6">
          <img src="images/photo-workplace.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">06</span><h3>衣料品製造・卸売・小売</h3></div>
        </a>
        <a href="it-services.html" class="biz-field-card reveal" data-delay="7">
          <img src="images/photo-office.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">07</span><h3>オフショア開発・ITアウトソーシング</h3></div>
        </a>
      </div>
    </div>
  </section>

  <section id="field-1" class="section-block">
    <div class="container biz-split">
      <div class="biz-content reveal-left">
        <span class="biz-field-num">01</span>
        <h2>外国人技能実習生・特定技能者の育成および送出し事業</h2>
        <p>当社は、外国人技能実習生および特定技能者の育成・送出しを行っております。</p>
        <ul class="biz-feature-list">
          <li>出国前の技能・日本語教育</li>
          <li>法的手続き・在留資格の支援</li>
          <li>実習・就労期間中のサポート</li>
          <li>受入企業との連携・研修プログラム提供</li>
        </ul>
        <p>外国人材の技能・経験・適応能力の向上を促進し、企業に対して高品質な人材の提供を実現しています。</p>
      </div>
      <div class="biz-image reveal-right">
        <img src="images/photo-workplace.jpg" alt="技能実習・特定技能">
      </div>
    </div>
  </section>

  <section id="field-2" class="section-block">
    <div class="container biz-split biz-split--reverse">
      <div class="biz-content reveal-right">
        <span class="biz-field-num">02</span>
        <h2>日本企業への人材紹介事業</h2>
        <p>技術・人文知識・国際業務ビザ対応の人材紹介サービスを提供しております。</p>
        <ul class="biz-feature-list">
          <li>技術（Engineering / 技術分野）</li>
          <li>人文知識・国際業務（Humanities / International Business）</li>
          <li>スキル・経験・日本語能力に適した人材の選定と紹介</li>
          <li>在留資格取得支援・受入れ体制整備コンサルティング</li>
        </ul>
      </div>
      <div class="biz-image reveal-left">
        <img src="images/photo-team.jpg" alt="高度人材紹介">
      </div>
    </div>
  </section>

  <section id="field-3" class="section-block">
    <div class="container">
      <div class="biz-split">
        <div class="biz-image reveal-left">
          <img src="images/photo-business.jpg" alt="登録支援機関">
        </div>
        <div class="biz-content reveal-right">
          <span class="biz-field-num">03</span>
          <h2>登録支援機関としての生活・就業支援サービス</h2>
          <p>「特定技能」は2019年4月に導入された在留資格で、人手不足が深刻な16業種で外国人労働者の受け入れが可能です。</p>
          <div class="industry-grid">
            <span class="industry-item">介護</span><span class="industry-item">ビルクリーニング</span>
            <span class="industry-item">工業製品製造業</span><span class="industry-item">建設</span>
            <span class="industry-item">造船・舶用工業</span><span class="industry-item">自動車整備</span>
            <span class="industry-item">航空</span><span class="industry-item">宿泊</span>
            <span class="industry-item">自動車運送業</span><span class="industry-item">鉄道</span>
            <span class="industry-item">農業</span><span class="industry-item">漁業</span>
            <span class="industry-item">飲食料品製造業</span><span class="industry-item">外食業</span>
            <span class="industry-item">林業</span><span class="industry-item">木材産業</span>
          </div>
          <h3>採用のメリット</h3>
          <div class="biz-benefit-grid">
            <div class="biz-benefit-card reveal" data-delay="1"><strong>メリット 1</strong>人材不足の解消</div>
            <div class="biz-benefit-card reveal" data-delay="2"><strong>メリット 2</strong>日本文化・日本語への理解</div>
            <div class="biz-benefit-card reveal" data-delay="3"><strong>メリット 3</strong>即戦力の採用</div>
          </div>
        </div>
      </div>

      <h3 class="reveal" style="text-align:center;margin-top:48px;color:var(--green-dark);">特定技能 外国人採用の流れ</h3>
      <div class="biz-steps">
        <div class="biz-step reveal" data-delay="1"><div class="biz-step-num">1</div><h4>人材募集・紹介</h4><p>ご要望をお伺いし最適な人材をご提案</p></div>
        <div class="biz-step reveal" data-delay="2"><div class="biz-step-num">2</div><h4>面接対応</h4><p>母国語スタッフが同行サポート</p></div>
        <div class="biz-step reveal" data-delay="3"><div class="biz-step-num">3</div><h4>内定・書類申請</h4><p>ビザ申請などトータルサポート</p></div>
        <div class="biz-step reveal" data-delay="4"><div class="biz-step-num">4</div><h4>入国準備</h4><p>生活環境整備を万全に</p></div>
        <div class="biz-step reveal" data-delay="5"><div class="biz-step-num">5</div><h4>就業開始</h4><p>定期的フォローアップ</p></div>
      </div>

      <div class="biz-point-grid">
        <div class="biz-point-card reveal" data-delay="1">
          <h4>POINT 1 – ワンストップ対応</h4>
          <p>人材選定から定着支援まで一貫したサービスを提供。即戦力となるベトナム人材を手間なく採用できます。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="2">
          <h4>POINT 2 – ベトナム語サポート</h4>
          <p>面接・生活指導・日常相談など、すべてベトナム語で対応可能な専門スタッフが常駐しています。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="3">
          <h4>POINT 3 – 法的手続き代行</h4>
          <p>特定技能・技術・人文知識・国際業務に関する全ての書類手続きを代行いたします。</p>
        </div>
      </div>
    </div>
  </section>

  <section id="field-4" class="section-block">
    <div class="container biz-split">
      <div class="biz-content reveal-left">
        <span class="biz-field-num">04</span>
        <h2>通訳・翻訳・研修・教育コンサルティング事業</h2>
        <p>言語および教育分野における包括的なサービスを提供しております。</p>
        <ul class="biz-feature-list">
          <li>通訳サービス：会議、研修、国際イベントでのコミュニケーション支援</li>
          <li>翻訳サービス：専門文書、契約書、マニュアル等の正確な翻訳</li>
          <li>研修事業：スキル研修、日本語教育、業務研修の実施</li>
          <li>教育コンサルティング：人材育成・スキル開発のアドバイス</li>
        </ul>
      </div>
      <div class="biz-image reveal-right">
        <img src="images/photo-meeting.jpg" alt="通訳・翻訳・研修">
      </div>
    </div>
  </section>

  <section id="field-5" class="section-block">
    <div class="container biz-split biz-split--reverse">
      <div class="biz-content reveal-right">
        <span class="biz-field-num">05</span>
        <h2>ベトナム企業・団体との国際連携および技術協力支援</h2>
        <p>日本とベトナム両国間における企業・団体・協会などとの国際的な連携および技術協力の促進を目的として活動しています。</p>
        <p>技術移転、人材育成、投資・生産分野での連携プロジェクトを支援し、建設業、機械産業、農業、人材開発などさまざまな分野での協力を推進してまいります。</p>
      </div>
      <div class="biz-image reveal-left">
        <img src="images/photo-network.jpg" alt="国際連携・技術協力">
      </div>
    </div>
  </section>

  <section id="field-6" class="section-block">
    <div class="container biz-split">
      <div class="biz-content reveal-left">
        <span class="biz-field-num">06</span>
        <h2>衣料品製造・卸売・小売事業</h2>
        <p>ベトナムおよび中国で製造された衣料品の卸売・小売を行い、日本市場向けに提供しております。</p>
        <ul class="biz-feature-list">
          <li><strong>高品質・トレンド重視</strong> — 品質管理徹底、最新トレンド対応</li>
          <li><strong>卸売・小売両対応</strong> — 店舗・オンライン・業者向け卸売</li>
          <li><strong>日本市場に最適化</strong> — サイズ感・デザインに合わせた商品選定</li>
          <li><strong>将来的な展望</strong> — 全国の消費者へ販売拡大</li>
        </ul>
      </div>
      <div class="biz-image reveal-right">
        <img src="images/photo-workplace.jpg" alt="衣料品事業">
      </div>
    </div>
  </section>

  <section id="field-7" class="section-block">
    <div class="container biz-split biz-split--reverse">
      <div class="biz-content reveal-right">
        <span class="biz-field-num">07</span>
        <h2>オフショア開発・ITアウトソーシング</h2>
        <p>ベトナムの優秀なITエンジニアと日本企業をつなぎ、日本市場のニーズに合わせたソフトウェア開発およびITアウトソーシングを提供しております。</p>
        <ul class="biz-feature-list">
          <li><strong>オフショア開発</strong> — 日本品質×合理コストで、要件定義から保守まで一貫対応</li>
          <li><strong>アプリケーション開発</strong> — Web・モバイル・業務システムの設計・実装</li>
          <li><strong>移行／クラウド／AI</strong> — レガシー刷新、クラウド活用、生成AI導入を支援</li>
          <li><strong>ERP・CRM／セキュリティ</strong> — 基幹・顧客管理とサイバーセキュリティ対策</li>
        </ul>
        <p>お客様のDX推進・業務効率化・新規サービス創出を力強くサポートいたします。</p>
        <a href="it-services.html" class="btn btn-primary" style="margin-top:20px;">ITサービスの詳細を見る</a>
      </div>
      <div class="biz-image reveal-left">
        <img src="images/photo-team.jpg" alt="オフショア開発チーム">
      </div>
    </div>
  </section>

  <section class="section-block section-cta-banner">
    <div class="container cta-inner reveal">
      <h2>事業に関するご相談はこちら</h2>
      <p>貴社のニーズに最適なサービスをご提案いたします</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-white">お問い合わせ</a>
        <a href="for-companies.html" class="btn btn-outline-white">企業様向け情報</a>
      </div>
    </div>
  </section>

</main>"""
    write_fullwidth_page("business.html", "事業内容", "business.html", content_html)

def build_for_companies() -> None:
    content_html = """<section class="hero hero--business">
  <img src="images/photo-meeting.jpg" alt="企業様へ" class="hero-image">
  <div class="hero-overlay"></div>
  <div class="hero-content reveal">
    <span class="hero-badge">For Companies</span>
    <h1>企業様へ</h1>
    <p>ベトナム人材と日本企業をつなぐ、信頼のパートナー</p>
  </div>
</section>

<main class="site-main site-main--business">

  <section class="section-block section-about">
    <div class="container about-split">
      <div class="about-text reveal-left">
        <span class="section-label">For Companies</span>
        <h2>日本企業の成長を支援する<br>外国人材紹介サービス</h2>
        <p>私たちの会社は、革新的な外国人材紹介サービスを通じて、日本企業の成長を支援しております。多様な文化やスキルを持つ人材を企業のニーズに合わせてマッチングすることで、国際的な競争力を高め、新たな可能性を創出します。</p>
        <p>ぜひ、私たちと共に未来を切り開いていきましょう。</p>
      </div>
      <div class="about-image reveal-right">
        <img src="images/photo-network.jpg" alt="ベトナム人材と日本企業をつなぐネットワーク">
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Talent Types</span>
        <h2>ご紹介可能な人材</h2>
        <p>技能実習生から高度人材まで、企業のニーズに合わせた人材をご提案</p>
      </div>
      <div class="biz-field-grid">
        <div class="biz-field-card reveal" data-delay="1">
          <img src="images/photo-workplace.jpg" alt="技能実習生">
          <div class="biz-field-card-body">
            <span class="biz-field-num">01</span>
            <h3>技能実習生</h3>
            <p>事前教育を経て、日本の現場で技能を習得・活躍する人材</p>
          </div>
        </div>
        <div class="biz-field-card reveal" data-delay="2">
          <img src="images/photo-business.jpg" alt="特定技能者">
          <div class="biz-field-card-body">
            <span class="biz-field-num">02</span>
            <h3>特定技能者</h3>
            <p>16業種で即戦力として活躍できる特定技能在留資格の人材</p>
          </div>
        </div>
        <div class="biz-field-card reveal" data-delay="3">
          <img src="images/photo-team.jpg" alt="高度人材">
          <div class="biz-field-card-body">
            <span class="biz-field-num">03</span>
            <h3>高度人材・技術者・専門家</h3>
            <p>技術・人文知識・国際業務ビザ対応の専門スキル人材</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container biz-split">
      <div class="biz-image reveal-left">
        <img src="images/photo-meeting.jpg" alt="企業様向けサポート">
      </div>
      <div class="biz-content reveal-right">
        <span class="section-label">Support</span>
        <h2>ベトナム人材と日本企業をつなぐ架け橋</h2>
        <p>当社は、ベトナム人材の日本企業への紹介サービスを専門に提供しております。企業様向けに以下のサポートを提供しております。</p>
        <ul class="biz-feature-list">
          <li>人材選定・マッチング</li>
          <li>研修・教育プログラムの提供</li>
          <li>法的手続きおよび在留資格（ビザ）取得支援</li>
          <li>受入れ後の人材管理・フォローアップ</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container biz-split biz-split--reverse">
      <div class="biz-content reveal-right">
        <span class="section-label">Talent Care</span>
        <h2>人材への育成・定着支援</h2>
        <p>ベトナム人材には日本語教育・専門スキル研修・生活指導を行い、日本での職場適応力向上と長期的なキャリア成長をサポートしております。</p>
        <div class="biz-support-grid">
          <div class="biz-support-item reveal" data-delay="1">
            <span class="biz-support-icon">01</span>
            <p>日本語教育・コミュニケーション研修</p>
          </div>
          <div class="biz-support-item reveal" data-delay="2">
            <span class="biz-support-icon">02</span>
            <p>専門スキル・業務研修プログラム</p>
          </div>
          <div class="biz-support-item reveal" data-delay="3">
            <span class="biz-support-icon">03</span>
            <p>生活指導・文化適応サポート</p>
          </div>
          <div class="biz-support-item reveal" data-delay="4">
            <span class="biz-support-icon">04</span>
            <p>キャリア相談・長期成長支援</p>
          </div>
        </div>
        <p>ベトナム・日本における広範なネットワークを活用し、企業様には質の高い人材の提供、人材には安心して働ける環境とキャリア形成の機会を提供いたします。</p>
      </div>
      <div class="biz-image reveal-left">
        <img src="images/photo-office.jpg" alt="人材育成・定着支援">
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Why KATAO</span>
        <h2>カタオ総合が選ばれる理由</h2>
      </div>
      <div class="biz-point-grid">
        <div class="biz-point-card reveal" data-delay="1">
          <h4>ワンストップ対応</h4>
          <p>人材選定から採用、入国後の生活・職場定着支援まで一貫したサービス。企業様は手間なく即戦力人材を採用できます。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="2">
          <h4>ベトナム語ネイティブサポート</h4>
          <p>面接・生活指導・日常相談など、すべてベトナム語で対応可能。スムーズなコミュニケーションを実現します。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="3">
          <h4>法的手続きのトータル代行</h4>
          <p>在留資格・ビザ申請から入国サポートまで、外国人雇用に必要な手続きをすべて代行いたします。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Process</span>
        <h2>採用の流れ</h2>
        <p>人材募集から就業開始まで5ステップで完全サポート</p>
      </div>
      <div class="biz-steps">
        <div class="biz-step reveal" data-delay="1"><div class="biz-step-num">1</div><h4>人材募集・紹介</h4><p>ご要望をお伺いし最適な人材をご提案</p></div>
        <div class="biz-step reveal" data-delay="2"><div class="biz-step-num">2</div><h4>面接対応</h4><p>母国語スタッフが同行サポート</p></div>
        <div class="biz-step reveal" data-delay="3"><div class="biz-step-num">3</div><h4>内定・書類申請</h4><p>ビザ申請などトータルサポート</p></div>
        <div class="biz-step reveal" data-delay="4"><div class="biz-step-num">4</div><h4>入国準備</h4><p>生活環境整備を万全に</p></div>
        <div class="biz-step reveal" data-delay="5"><div class="biz-step-num">5</div><h4>就業開始</h4><p>定期的フォローアップ</p></div>
      </div>
    </div>
  </section>

  <section class="section-block section-cta-banner">
    <div class="container cta-inner reveal">
      <h2>まずはお気軽にご相談ください</h2>
      <p>貴社の人材課題に最適なソリューションをご提案いたします</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-white">お問い合わせ</a>
        <a href="business.html" class="btn btn-outline-white">事業内容を見る</a>
      </div>
    </div>
  </section>

</main>"""
    write_fullwidth_page("for-companies.html", "企業様へ", "for-companies.html", content_html)

def build_recruitment() -> None:
    content_html = """<section class="hero hero--business">
  <img src="images/photo-team.jpg" alt="採用情報" class="hero-image">
  <div class="hero-overlay"></div>
  <div class="hero-content reveal">
    <span class="hero-badge">Recruitment</span>
    <h1>採用情報</h1>
    <p>国際人材の架け橋として、共に未来を築きませんか</p>
  </div>
</section>

<main class="site-main site-main--business">

  <section class="section-block section-about">
    <div class="container about-split">
      <div class="about-text reveal-left">
        <span class="section-label">Join Us</span>
        <h2>株式会社カタオ総合で<br>一緒に働きませんか？</h2>
        <p>私たち株式会社カタオ総合は、ベトナム人材の育成・紹介、外国人技能実習生・特定技能者のサポート、通訳・翻訳・教育コンサルティングなど、多岐にわたる事業を展開しています。</p>
        <p>国際的な視点を持ち、日本企業と海外人材の架け橋となるやりがいのある仕事に挑戦しませんか？</p>
      </div>
      <div class="about-image reveal-right">
        <img src="images/photo-workplace.jpg" alt="チームで働く環境">
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Open Positions</span>
        <h2>募集職種</h2>
        <p>あなたのスキルと経験を活かせるポジションをご用意しています</p>
      </div>
      <div class="recruit-job-grid">
        <div class="recruit-job-card reveal" data-delay="1">
          <img src="images/photo-meeting.jpg" alt="人材コーディネーター">
          <div class="recruit-job-body">
            <span class="biz-field-num">01</span>
            <h3>人材コーディネーター / キャリアアドバイザー</h3>
            <ul>
              <li>外国人材の採用・紹介・フォローアップ業務</li>
              <li>日本企業と外国人材のマッチングサポート</li>
              <li>日本語・ベトナム語対応可能な方歓迎</li>
            </ul>
          </div>
        </div>
        <div class="recruit-job-card reveal" data-delay="2">
          <img src="images/photo-business.jpg" alt="通訳・翻訳スタッフ">
          <div class="recruit-job-body">
            <span class="biz-field-num">02</span>
            <h3>通訳・翻訳スタッフ</h3>
            <ul>
              <li>会議、研修、契約書類などの通訳・翻訳業務</li>
              <li>日本語とベトナム語に精通した方</li>
            </ul>
          </div>
        </div>
        <div class="recruit-job-card reveal" data-delay="3">
          <img src="images/photo-office.jpg" alt="事務・総務スタッフ">
          <div class="recruit-job-body">
            <span class="biz-field-num">03</span>
            <h3>事務・総務スタッフ</h3>
            <ul>
              <li>採用・入国手続きサポート</li>
              <li>書類作成、社内管理業務</li>
            </ul>
          </div>
        </div>
        <div class="recruit-job-card reveal" data-delay="4">
          <img src="images/photo-network.jpg" alt="営業・営業企画">
          <div class="recruit-job-body">
            <span class="biz-field-num">04</span>
            <h3>営業・営業企画</h3>
            <ul>
              <li>日本企業向け人材提案・衣料品販売</li>
              <li>市場調査、販路開拓</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Ideal Candidate</span>
        <h2>求める人物像</h2>
      </div>
      <div class="biz-benefit-grid biz-benefit-grid--4">
        <div class="biz-benefit-card reveal" data-delay="1"><strong>グローバル視点</strong>チームで協力できる方</div>
        <div class="biz-benefit-card reveal" data-delay="2"><strong>挑戦意欲</strong>新しいことに挑戦する意欲がある方</div>
        <div class="biz-benefit-card reveal" data-delay="3"><strong>語学力</strong>日本語・ベトナム語を活用できる方</div>
        <div class="biz-benefit-card reveal" data-delay="4"><strong>情熱</strong>国際交流や人材育成に興味がある方</div>
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container biz-split">
      <div class="biz-content reveal-left">
        <span class="section-label">Conditions</span>
        <h2>勤務条件</h2>
        <div class="recruit-conditions">
          <div class="recruit-condition-item reveal" data-delay="1">
            <span class="recruit-condition-label">勤務地</span>
            <span class="recruit-condition-value">東京都足立区加賀1-7-5</span>
          </div>
          <div class="recruit-condition-item reveal" data-delay="2">
            <span class="recruit-condition-label">勤務時間</span>
            <span class="recruit-condition-value">9:00〜18:00（フレックスタイム応相談）</span>
          </div>
          <div class="recruit-condition-item reveal" data-delay="3">
            <span class="recruit-condition-label">給与</span>
            <span class="recruit-condition-value">経験・能力を考慮の上、当社規定により優遇</span>
          </div>
          <div class="recruit-condition-item reveal" data-delay="4">
            <span class="recruit-condition-label">休日休暇</span>
            <span class="recruit-condition-value">土日祝日、年末年始、有給休暇</span>
          </div>
        </div>
      </div>
      <div class="biz-image reveal-right">
        <img src="images/photo-office.jpg" alt="勤務環境">
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="recruit-apply reveal">
        <span class="section-label">Apply</span>
        <h2>応募方法</h2>
        <p>下記の書類をメールまたは郵送にてお送りください。</p>
        <ul class="biz-feature-list">
          <li>履歴書（写真貼付）</li>
          <li>職務経歴書（任意）</li>
        </ul>
        <div class="recruit-apply-contact">
          <span class="contact-label">応募先メール</span>
          <a href="mailto:kataosogo.info@gmail.com" class="contact-value">kataosogo.info@gmail.com</a>
          <p class="recruit-apply-note">件名：<strong>採用応募（氏名）</strong></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container biz-split biz-split--reverse">
      <div class="biz-content reveal-right">
        <span class="section-label">Message</span>
        <h2>私たちからのメッセージ</h2>
        <p>私たちは、社員一人ひとりの成長を支え、挑戦する環境を提供しています。国際人材・人材育成・教育・販売など、多彩な事業に携わることで、キャリアの幅を広げることができます。</p>
        <p>あなたの力を、株式会社カタオ総合で発揮してください。</p>
      </div>
      <div class="biz-image reveal-left">
        <img src="images/photo-meeting.jpg" alt="チームメッセージ">
      </div>
    </div>
  </section>

  <section class="section-block section-cta-banner">
    <div class="container cta-inner reveal">
      <h2>ご応募お待ちしております</h2>
      <p>ご質問がある方もお気軽にお問い合わせください</p>
      <div class="hero-actions">
        <a href="mailto:kataosogo.info@gmail.com" class="btn btn-white">メールで応募</a>
        <a href="contact.html" class="btn btn-outline-white">お問い合わせ</a>
      </div>
    </div>
  </section>

</main>"""
    write_fullwidth_page("recruitment.html", "採用情報", "recruitment.html", content_html)

def build_jobs() -> None:
    body_html = """
    <article class="section">
      <div class="job-card">
        <h2>技術・人文知識・国際業務ビザ人材（Engineer / Specialist）</h2>
        <p>専門知識と実務経験を活かし、日本企業での中長期的なキャリア形成を目指す方向けの求人カテゴリです。</p>
      </div>
      <div class="job-card">
        <h2>特定技能者（Specified Skilled Worker）</h2>
        <p>特定技能制度の対象分野で、即戦力として活躍したい方向けの求人カテゴリです。</p>
      </div>
    </article>
    """
    write_page("jobs.html", "求人情報", "jobs.html", body_html, page_hero("求人情報", "Job Openings"))


def build_news() -> None:
    body_html = """
    <article class="section">
      <p>現在、掲載中のニュースはありません。</p>
      <p>新着情報は準備が整い次第、こちらのページでお知らせします。</p>
    </article>
    """
    write_page("news.html", "ニュース", "news.html", body_html, page_hero("ニュース", "News"))


def build_contact() -> None:
    body_html = """
    <article class="section contact-page">
      <h1>お問い合わせ</h1>
      <p>ご質問・ご相談は、下記の連絡先までお気軽にお問い合わせください。</p>
      <div class="contact-info">
        <div class="contact-card reveal">
          <span class="contact-label">電話番号</span>
          <a href="tel:0363362753" class="contact-value">03-6336-2753</a>
        </div>
        <div class="contact-card reveal" data-delay="1">
          <span class="contact-label">メールアドレス</span>
          <a href="mailto:kataosogo.info@gmail.com" class="contact-value">kataosogo.info@gmail.com</a>
        </div>
      </div>
    </article>
    """
    write_page("contact.html", "お問い合わせ", "contact.html", body_html)


def _it_service_cards_html(exclude_slug=None) -> str:
    cards = []
    for i, svc in enumerate(IT_SERVICES, start=1):
        if exclude_slug and svc["slug"] == exclude_slug:
            continue
        cards.append(
            f"""        <a href="{svc['slug']}.html" class="biz-field-card reveal" data-delay="{(i % 4) + 1}">
          <img src="images/{svc['image']}" alt="{svc['title']}">
          <div class="biz-field-card-body">
            <span class="biz-field-num">{svc['num']}</span>
            <h3>{svc['title']}</h3>
            <p>{svc['summary']}</p>
          </div>
        </a>"""
        )
    return "\n".join(cards)


def build_it_services() -> None:
    cards = _it_service_cards_html()
    content_html = f"""<section class="hero hero--business">
  <img src="images/photo-team.jpg" alt="ITアウトソーシング" class="hero-image">
  <div class="hero-overlay"></div>
  <div class="hero-content reveal">
    <span class="hero-badge">IT Outsourcing</span>
    <h1>ITアウトソーシング</h1>
    <p>オフショア開発からAI・セキュリティまで、DXをトータル支援</p>
  </div>
</section>

<main class="site-main site-main--business">

  <section class="section-block section-about">
    <div class="container about-split">
      <div class="about-text reveal-left">
        <span class="section-label">Overview</span>
        <h2>日本品質のITを、<br>合理的なコストで</h2>
        <p>株式会社カタオ総合は、ベトナムの優秀なエンジニアリングリソースと日本側のブリッジ体制を組み合わせ、企業のDX・システム開発・運用課題を解決します。</p>
        <p>アプリケーション開発、システム移行、クラウド、AI／生成AI、ERP・CRM、サイバーセキュリティまで、要件定義から保守運用までワンストップでご支援します。</p>
      </div>
      <div class="about-image reveal-right">
        <img src="images/photo-office.jpg" alt="ITアウトソーシング概要">
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Our Services</span>
        <h2>提供サービス</h2>
        <p>8つのITサービスで、企画から運用までをトータルサポート</p>
      </div>
      <div class="biz-field-grid">
{cards}
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Why Us</span>
        <h2>選ばれる理由</h2>
      </div>
      <div class="biz-point-grid">
        <div class="biz-point-card reveal" data-delay="1">
          <h4>POINT 1 – ブリッジSE体制</h4>
          <p>日本語・ベトナム語・英語での丁寧なコミュニケーションにより、要件の齟齬を最小化します。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="2">
          <h4>POINT 2 – 日本品質×コスト効率</h4>
          <p>レビュー・テスト・納品基準を日本水準で運用しつつ、オフショアのコストメリットを活かします。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="3">
          <h4>POINT 3 – 一気通貫サポート</h4>
          <p>開発だけでなく、移行・クラウド・AI・保守運用・セキュリティまで継続的に伴走します。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-block section-cta-banner">
    <div class="container cta-inner reveal">
      <h2>ITアウトソーシングのご相談</h2>
      <p>貴社の課題に最適なサービスをご提案いたします</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-white">お問い合わせ</a>
        <a href="business.html" class="btn btn-outline-white">事業内容を見る</a>
      </div>
    </div>
  </section>

</main>"""
    write_fullwidth_page("it-services.html", "ITアウトソーシング", "it-services.html", content_html)


def build_it_service_details() -> None:
    for svc in IT_SERVICES:
        features_html = "\n".join(
            f'          <li><strong>{title}</strong> — {desc}</li>'
            for title, desc in svc["features"]
        )
        process_html = "\n".join(
            f'        <div class="biz-step reveal" data-delay="{i}"><div class="biz-step-num">{i}</div><h4>{title}</h4><p>{desc}</p></div>'
            for i, (title, desc) in enumerate(svc["process"], start=1)
        )
        benefits_html = "\n".join(
            f'          <div class="biz-benefit-card reveal" data-delay="{i}"><strong>メリット {i}</strong>{b}</div>'
            for i, b in enumerate(svc["benefits"], start=1)
        )
        related = _it_service_cards_html(exclude_slug=svc["slug"])

        content_html = f"""<section class="hero hero--business">
  <img src="images/{svc['image']}" alt="{svc['title']}" class="hero-image">
  <div class="hero-overlay"></div>
  <div class="hero-content reveal">
    <span class="hero-badge">{svc['en']}</span>
    <h1>{svc['title']}</h1>
    <p>{svc['summary']}</p>
  </div>
</section>

<main class="site-main site-main--business">

  <section class="section-block">
    <div class="container">
      <nav class="breadcrumb reveal" aria-label="パンくず">
        <a href="index.html">ホーム</a>
        <span>/</span>
        <a href="it-services.html">ITアウトソーシング</a>
        <span>/</span>
        <span>{svc['title']}</span>
      </nav>
    </div>
  </section>

  <section class="section-block section-about">
    <div class="container about-split">
      <div class="about-text reveal-left">
        <span class="section-label">{svc['num']} — Detail</span>
        <h2>{svc['title']}</h2>
        <p>{svc['lead']}</p>
        <ul class="biz-feature-list">
{features_html}
        </ul>
      </div>
      <div class="about-image reveal-right">
        <img src="images/{svc['image']}" alt="{svc['title']}">
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Process</span>
        <h2>ご支援の流れ</h2>
      </div>
      <div class="biz-steps">
{process_html}
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Benefits</span>
        <h2>導入メリット</h2>
      </div>
      <div class="biz-benefit-grid">
{benefits_html}
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Related Services</span>
        <h2>関連サービス</h2>
        <p>あわせてご検討いただけるITサービス</p>
      </div>
      <div class="biz-field-grid">
{related}
      </div>
    </div>
  </section>

  <section class="section-block section-cta-banner">
    <div class="container cta-inner reveal">
      <h2>{svc['title']}に関するご相談</h2>
      <p>まずはお気軽にお問い合わせください。課題に合わせたご提案をいたします。</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-white">お問い合わせ</a>
        <a href="it-services.html" class="btn btn-outline-white">サービス一覧へ</a>
      </div>
    </div>
  </section>

</main>"""
        write_fullwidth_page(
            f"{svc['slug']}.html",
            svc["title"],
            f"{svc['slug']}.html",
            content_html,
        )


def main() -> None:
    print("Generating kataosogo-site pages...")
    build_home()
    build_company()
    build_greeting()
    build_business()
    build_it_services()
    build_it_service_details()
    build_for_companies()
    build_recruitment()
    build_jobs()
    build_news()
    build_contact()
    print("Done.")


if __name__ == "__main__":
    main()
