#!/usr/bin/env python3
"""Generate all static HTML pages for a kataosogo.jp clone."""

import json
from pathlib import Path
from textwrap import dedent

from i18n_pages import to_lang_dicts

OUT_DIR = Path(__file__).resolve().parent

# (href, i18n key, default JA label)
NAV_ITEMS = [
    ("index.html", "nav.home", "ホーム"),
    ("company.html", "nav.company", "会社概要"),
    ("greeting.html", "nav.greeting", "代表者挨拶"),
    ("business.html", "nav.business", "事業内容"),
    ("it-services.html", "nav.it", "ITサービス"),
    ("for-companies.html", "nav.forCompanies", "企業様へ"),
    ("recruitment.html", "nav.recruitment", "採用情報"),
    ("jobs.html", "nav.jobs", "求人情報"),
    ("news.html", "nav.news", "ニュース"),
]

LANG_SWITCH_HTML = """\
                <div class="lang-switch" role="group" data-i18n-aria="lang.label" aria-label="言語">
                  <button type="button" class="lang-btn is-active" data-lang="ja" aria-pressed="true">日本語</button>
                  <button type="button" class="lang-btn" data-lang="vi" aria-pressed="false">VI</button>
                </div>"""

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
        "title_vi": "Phát triển offshore",
        "en": "Offshore Development",
        "summary": "ベトナムの優秀なITエンジニアと日本企業をつなぎ、日本品質×合理コストの開発を実現",
        "summary_vi": "Kết nối kỹ sư IT xuất sắc tại Việt Nam với doanh nghiệp Nhật — chất lượng Nhật × chi phí hợp lý",
        "image": "photo-team.jpg",
        "lead": "ベトナム拠点のエンジニアリング力と、日本側のブリッジ体制を組み合わせ、要件定義からリリース・保守まで一貫して対応します。コミュニケーションロスを抑えつつ、開発スピードとコスト効率を両立します。",
        "lead_vi": "Kết hợp năng lực kỹ thuật tại Việt Nam với đội ngũ bridge phía Nhật, hỗ trợ xuyên suốt từ định nghĩa yêu cầu đến release và bảo trì. Giảm mất mát giao tiếp, đồng thời cân bằng tốc độ phát triển và hiệu quả chi phí.",
        "features": [
            ("ブリッジSE体制", "日本語・ベトナム語・英語での円滑なコミュニケーションと進捗管理"),
            ("ラボ型／請負型", "専属チームによるラボ開発、または要件固定の請負開発に対応"),
            ("日本品質の工程管理", "設計レビュー・コードレビュー・テスト・納品基準を日本基準で運用"),
            ("柔軟なスケール", "プロジェクト規模に応じてチーム規模を拡大・縮小可能"),
        ],
        "features_vi": [
            ("Đội ngũ Bridge SE", "Giao tiếp và quản lý tiến độ trơn tru bằng tiếng Nhật·Việt·Anh"),
            ("Lab / thầu khoán", "Phát triển lab với đội chuyên trách, hoặc thầu khoán theo yêu cầu cố định"),
            ("Quản lý quy trình chuẩn Nhật", "Review thiết kế·code·test·tiêu chuẩn bàn giao theo chuẩn Nhật"),
            ("Scale linh hoạt", "Mở rộng hoặc thu hẹp đội theo quy mô dự án"),
        ],
        "process": [
            ("ヒアリング", "課題・予算・スケジュールの整理"),
            ("提案・見積", "体制・技術・コストのご提案"),
            ("キックオフ", "チーム編成と開発ルールの合意"),
            ("開発・検証", "アジャイル／ウォーターフォール対応"),
            ("納品・運用", "移行支援と継続改善"),
        ],
        "process_vi": [
            ("Lắng nghe", "Làm rõ thách thức·ngân sách·lịch trình"),
            ("Đề xuất·báo giá", "Đề xuất tổ chức·công nghệ·chi phí"),
            ("Kick-off", "Thống nhất đội ngũ và quy tắc phát triển"),
            ("Phát triển·kiểm thử", "Hỗ trợ Agile / Waterfall"),
            ("Bàn giao·vận hành", "Hỗ trợ chuyển đổi và cải tiến liên tục"),
        ],
        "benefits": [
            "優秀なベトナムIT人材を、日本品質の管理体制で活用",
            "国内開発と比べてコストを抑えつつスピードを確保",
            "要件の曖昧さにも対応できるブリッジSEサポート",
        ],
        "benefits_vi": [
            "Tận dụng nhân sự IT Việt trong khung quản lý chất lượng Nhật",
            "Giữ tốc độ và kiểm soát chi phí so với phát triển trong nước",
            "Bridge SE hỗ trợ cả khi yêu cầu còn chưa rõ ràng",
        ],
    },
    {
        "slug": "application-development",
        "num": "02",
        "title": "アプリケーション開発",
        "title_vi": "Phát triển ứng dụng",
        "en": "Application Development",
        "summary": "Web・モバイル・業務システムなど、ビジネス要件に最適化したアプリ開発",
        "summary_vi": "Phát triển ứng dụng tối ưu yêu cầu kinh doanh — Web·mobile·hệ thống nghiệp vụ",
        "image": "photo-office.jpg",
        "lead": "新規サービス立ち上げから既存システムの刷新まで、企画・設計・実装・テスト・リリースをワンストップで支援します。モダンな技術スタックと堅実な品質管理で、使いやすく保守しやすいアプリケーションを構築します。",
        "lead_vi": "Từ khởi tạo dịch vụ mới đến làm mới hệ thống hiện có, hỗ trợ one-stop lập kế hoạch·thiết kế·triển khai·test·release. Với stack hiện đại và quản lý chất lượng vững chắc, xây dựng ứng dụng dễ dùng và dễ bảo trì.",
        "features": [
            ("Webアプリケーション", "業務ポータル、SaaS、社内システム、API連携など"),
            ("モバイルアプリ", "iOS / Android（ネイティブ・クロスプラットフォーム）"),
            ("業務システム", "受発注・在庫・勤怠・顧客管理などのカスタム開発"),
            ("UI/UX設計", "現場の業務フローに沿った画面設計と操作性の最適化"),
        ],
        "features_vi": [
            ("Ứng dụng Web", "Portal nghiệp vụ, SaaS, hệ thống nội bộ, liên kết API…"),
            ("Ứng dụng mobile", "iOS / Android (native·cross-platform)"),
            ("Hệ thống nghiệp vụ", "Custom đặt hàng·tồn kho·chấm công·CRM…"),
            ("Thiết kế UI/UX", "Tối ưu màn hình và trải nghiệm theo quy trình hiện trường"),
        ],
        "process": [
            ("要件定義", "業務課題と機能要件の明確化"),
            ("設計", "アーキテクチャ・画面・データ設計"),
            ("実装", "アジャイル開発と定期デモ"),
            ("テスト", "単体・結合・受け入れ試験"),
            ("リリース", "本番展開と初期サポート"),
        ],
        "process_vi": [
            ("Định nghĩa yêu cầu", "Làm rõ thách thức nghiệp vụ và chức năng"),
            ("Thiết kế", "Kiến trúc·màn hình·dữ liệu"),
            ("Triển khai", "Phát triển Agile và demo định kỳ"),
            ("Kiểm thử", "Unit·integration·UAT"),
            ("Release", "Triển khai production và hỗ trợ ban đầu"),
        ],
        "benefits": [
            "ビジネス目標に直結する機能設計",
            "将来の拡張・保守を見据えたアーキテクチャ",
            "オフショア体制によるコスト効率の高い開発",
        ],
        "benefits_vi": [
            "Thiết kế chức năng gắn trực tiếp mục tiêu kinh doanh",
            "Kiến trúc hướng tới mở rộng và bảo trì lâu dài",
            "Phát triển hiệu quả chi phí nhờ mô hình offshore",
        ],
    },
    {
        "slug": "migration",
        "num": "03",
        "title": "移行",
        "title_vi": "Chuyển đổi hệ thống",
        "en": "System Migration",
        "summary": "レガシーシステムからクラウド／新基盤への安全・確実な移行支援",
        "summary_vi": "Hỗ trợ chuyển đổi an toàn·chắc chắn từ legacy sang cloud / nền tảng mới",
        "image": "photo-network.jpg",
        "lead": "古い基幹システムやオンプレミス環境の刷新、クラウド移行、データ移行まで、ダウンタイムとリスクを最小化しながら段階的に進めます。現状分析から移行計画、リハーサル、本番切替、安定化まで一貫して伴走します。",
        "lead_vi": "Từ làm mới hệ thống lõi cũ hoặc on-premise, chuyển cloud, đến migration dữ liệu — tiến hành theo giai đoạn, giảm downtime và rủi ro. Đồng hành từ phân tích hiện trạng, kế hoạch, rehearsal, cutover đến ổn định.",
        "features": [
            ("レガシー刷新", "老朽化した業務システム・基幹系の再構築／リライト"),
            ("クラウド移行", "オンプレミスからAWS／Azure／GCP等への移行"),
            ("データ移行", "データクレンジング、マッピング、検証、切替計画"),
            ("並行稼働支援", "段階移行・ロールバック設計によるリスク低減"),
        ],
        "features_vi": [
            ("Làm mới legacy", "Tái xây dựng / rewrite hệ thống nghiệp vụ·lõi đã cũ"),
            ("Chuyển cloud", "Từ on-premise sang AWS / Azure / GCP…"),
            ("Migration dữ liệu", "Làm sạch, mapping, kiểm chứng, kế hoạch chuyển đổi"),
            ("Hỗ trợ chạy song song", "Giảm rủi ro bằng chuyển giai đoạn và thiết kế rollback"),
        ],
        "process": [
            ("現状分析", "資産・依存関係・リスクの棚卸し"),
            ("移行計画", "方式・スケジュール・切替戦略の策定"),
            ("構築・検証", "新環境構築と移行リハーサル"),
            ("本番切替", "計画的なカットオーバー"),
            ("安定化", "監視・障害対応・最適化"),
        ],
        "process_vi": [
            ("Phân tích hiện trạng", "Rà soát tài sản·phụ thuộc·rủi ro"),
            ("Kế hoạch chuyển đổi", "Phương án·lịch trình·chiến lược cutover"),
            ("Xây dựng·kiểm chứng", "Môi trường mới và rehearsal migration"),
            ("Cutover production", "Chuyển đổi theo kế hoạch"),
            ("Ổn định", "Giám sát·xử lý sự cố·tối ưu"),
        ],
        "benefits": [
            "移行リスクと業務停止時間の最小化",
            "将来の運用コスト削減と拡張性の向上",
            "技術負債の解消とセキュリティ強化",
        ],
        "benefits_vi": [
            "Giảm thiểu rủi ro chuyển đổi và thời gian gián đoạn nghiệp vụ",
            "Giảm chi phí vận hành dài hạn và tăng khả năng mở rộng",
            "Giảm nợ kỹ thuật và tăng cường bảo mật",
        ],
    },
    {
        "slug": "maintenance-operations",
        "num": "04",
        "title": "保守＆運用支援",
        "title_vi": "Bảo trì & hỗ trợ vận hành",
        "en": "Maintenance & Operations",
        "summary": "システムの安定稼働を支える、監視・障害対応・改善の継続サポート",
        "summary_vi": "Hỗ trợ liên tục giám sát·xử lý sự cố·cải tiến để hệ thống vận hành ổn định",
        "image": "photo-business.jpg",
        "lead": "開発後も安心してご利用いただけるよう、障害対応、定期メンテナンス、性能改善、小規模改修まで運用チームが継続支援します。SLAに応じた対応体制で、ビジネスの止まらないIT基盤を維持します。",
        "lead_vi": "Sau phát triển, đội vận hành tiếp tục hỗ trợ xử lý sự cố, bảo trì định kỳ, cải thiện hiệu năng và chỉnh sửa nhỏ. Với SLA phù hợp, duy trì nền tảng IT không gián đoạn kinh doanh.",
        "features": [
            ("監視・アラート", "可用性・性能・エラーの常時監視と一次対応"),
            ("障害対応", "原因調査、応急措置、恒久対策まで迅速に対応"),
            ("定期保守", "パッチ適用、バックアップ確認、脆弱性対応"),
            ("改善・改修", "運用改善提案と小規模機能追加"),
        ],
        "features_vi": [
            ("Giám sát·cảnh báo", "Theo dõi liên tục availability·hiệu năng·lỗi và xử lý sơ bộ"),
            ("Xử lý sự cố", "Điều tra nguyên nhân, biện pháp tạm thời đến giải pháp lâu dài"),
            ("Bảo trì định kỳ", "Patch, kiểm tra backup, xử lý lỗ hổng"),
            ("Cải tiến·chỉnh sửa", "Đề xuất cải thiện vận hành và bổ sung chức năng nhỏ"),
        ],
        "process": [
            ("引き継ぎ", "システム構成・運用手順の把握"),
            ("体制設計", "窓口・SLA・エスカレーションの定義"),
            ("運用開始", "監視・問い合わせ対応の開始"),
            ("定期報告", "稼働状況と改善提案の共有"),
            ("継続改善", "コスト最適化と品質向上"),
        ],
        "process_vi": [
            ("Bàn giao", "Nắm cấu trúc hệ thống và quy trình vận hành"),
            ("Thiết kế tổ chức", "Định nghĩa đầu mối·SLA·escalation"),
            ("Bắt đầu vận hành", "Giám sát và tiếp nhận yêu cầu"),
            ("Báo cáo định kỳ", "Chia sẻ tình trạng vận hành và đề xuất cải tiến"),
            ("Cải tiến liên tục", "Tối ưu chi phí và nâng cao chất lượng"),
        ],
        "benefits": [
            "社内ITリソースの負荷軽減",
            "障害時の迅速な復旧と再発防止",
            "運用データを活かした継続的な改善",
        ],
        "benefits_vi": [
            "Giảm tải cho nguồn lực IT nội bộ",
            "Khôi phục nhanh khi sự cố và ngăn tái diễn",
            "Cải tiến liên tục dựa trên dữ liệu vận hành",
        ],
    },
    {
        "slug": "cloud-computing",
        "num": "05",
        "title": "クラウドコンピューティング",
        "title_vi": "Điện toán đám mây",
        "en": "Cloud Computing",
        "summary": "設計・構築・最適化まで、クラウド活用をトータルで支援",
        "summary_vi": "Hỗ trợ toàn diện tận dụng cloud — từ thiết kế·xây dựng đến tối ưu",
        "image": "photo-office.jpg",
        "lead": "クラウドの導入検討からアーキテクチャ設計、構築、コスト最適化、運用までを支援します。セキュリティと可用性を両立したクラウド基盤で、スケーラブルなビジネス成長を支えます。",
        "lead_vi": "Hỗ trợ từ đánh giá triển khai cloud, thiết kế kiến trúc, xây dựng, tối ưu chi phí đến vận hành. Nền tảng cloud cân bằng bảo mật và availability, hỗ trợ tăng trưởng kinh doanh có thể scale.",
        "features": [
            ("クラウド設計・構築", "AWS / Azure / GCP を活用した基盤構築"),
            ("コンテナ／サーバレス", "Docker、Kubernetes、Functions 等の活用"),
            ("コスト最適化", "利用状況分析とリソース最適化"),
            ("セキュリティ設計", "IAM、ネットワーク、暗号化、監査ログの整備"),
        ],
        "features_vi": [
            ("Thiết kế·xây dựng cloud", "Xây nền tảng với AWS / Azure / GCP"),
            ("Container / serverless", "Tận dụng Docker, Kubernetes, Functions…"),
            ("Tối ưu chi phí", "Phân tích sử dụng và tối ưu tài nguyên"),
            ("Thiết kế bảo mật", "IAM, mạng, mã hóa, nhật ký kiểm toán"),
        ],
        "process": [
            ("アセスメント", "現状課題とクラウド適合性の評価"),
            ("設計", "構成・セキュリティ・コスト設計"),
            ("構築", "インフラ／アプリ基盤の実装"),
            ("移行・展開", "段階的な本番展開"),
            ("運用最適化", "監視・FinOps・改善"),
        ],
        "process_vi": [
            ("Assessment", "Đánh giá thách thức hiện tại và độ phù hợp cloud"),
            ("Thiết kế", "Cấu trúc·bảo mật·chi phí"),
            ("Xây dựng", "Triển khai hạ tầng / nền tảng ứng dụng"),
            ("Chuyển đổi·triển khai", "Triển khai production theo giai đoạn"),
            ("Tối ưu vận hành", "Giám sát·FinOps·cải tiến"),
        ],
        "benefits": [
            "初期投資を抑えつつ迅速にスケール可能",
            "可用性と災害対策の強化",
            "運用自動化による人的負荷の削減",
        ],
        "benefits_vi": [
            "Scale nhanh với đầu tư ban đầu thấp hơn",
            "Tăng availability và khả năng chống thảm họa",
            "Giảm tải con người nhờ tự động hóa vận hành",
        ],
    },
    {
        "slug": "ai-genai",
        "num": "06",
        "title": "AI / Gen AI",
        "title_vi": "AI / Gen AI",
        "en": "AI & Generative AI",
        "summary": "業務効率化・顧客体験向上に繋がるAI／生成AIソリューションの導入支援",
        "summary_vi": "Hỗ trợ triển khai AI / GenAI gắn với hiệu quả vận hành và trải nghiệm khách hàng",
        "image": "photo-meeting.jpg",
        "lead": "チャットボット、文書要約、画像認識、需要予測など、生成AI・機械学習を実務に落とし込みます。PoCから本番導入、ガバナンス整備まで、安全かつ効果的なAI活用を支援します。",
        "lead_vi": "Đưa GenAI và machine learning vào thực tế: chatbot, tóm tắt tài liệu, nhận dạng ảnh, dự báo nhu cầu… Từ PoC đến production và thiết lập governance — hỗ trợ dùng AI an toàn và hiệu quả.",
        "features": [
            ("生成AI活用", "社内FAQ、文書作成支援、ナレッジ検索、業務自動化"),
            ("機械学習", "予測・分類・レコメンドなどのモデル構築"),
            ("LLM連携開発", "API連携、RAG、社内データとの安全な接続"),
            ("AIガバナンス", "セキュリティ、個人情報、利用ポリシーの整備"),
        ],
        "features_vi": [
            ("Ứng dụng GenAI", "FAQ nội bộ, hỗ trợ soạn thảo, tìm kiếm knowledge, tự động hóa nghiệp vụ"),
            ("Machine learning", "Xây mô hình dự báo·phân loại·recommend"),
            ("Phát triển liên kết LLM", "API, RAG, kết nối an toàn với dữ liệu nội bộ"),
            ("AI governance", "Bảo mật, dữ liệu cá nhân, chính sách sử dụng"),
        ],
        "process": [
            ("ユースケース選定", "効果と実現性の高い課題の特定"),
            ("PoC", "小規模検証で効果を確認"),
            ("本開発", "本番品質のシステム化"),
            ("導入・教育", "現場展開と運用ルール整備"),
            ("効果測定", "KPIモニタリングと改善"),
        ],
        "process_vi": [
            ("Chọn use case", "Xác định bài toán hiệu quả và khả thi"),
            ("PoC", "Xác nhận hiệu quả qua thử nghiệm nhỏ"),
            ("Phát triển chính", "Hệ thống hóa chất lượng production"),
            ("Triển khai·đào tạo", "Triển khai hiện trường và quy tắc vận hành"),
            ("Đo lường hiệu quả", "Theo dõi KPI và cải tiến"),
        ],
        "benefits": [
            "定型業務の自動化と生産性向上",
            "顧客対応品質・スピードの改善",
            "データに基づく意思決定の高度化",
        ],
        "benefits_vi": [
            "Tự động hóa công việc lặp lại và tăng năng suất",
            "Cải thiện chất lượng·tốc độ chăm sóc khách hàng",
            "Nâng cao quyết định dựa trên dữ liệu",
        ],
    },
    {
        "slug": "erp-crm",
        "num": "07",
        "title": "ERP - CRM",
        "title_vi": "ERP - CRM",
        "en": "ERP & CRM",
        "summary": "基幹業務と顧客管理を統合し、経営の可視化と営業生産性を向上",
        "summary_vi": "Tích hợp nghiệp vụ lõi và quản lý khách hàng — tăng khả năng nhìn thấy quản trị và năng suất bán hàng",
        "image": "photo-workplace.jpg",
        "lead": "ERP／CRMの導入・カスタマイズ・周辺連携・データ移行までを支援します。部門ごとに分断された業務データを統合し、経営判断と現場オペレーションの両方を強化します。",
        "lead_vi": "Hỗ trợ triển khai·custom ERP/CRM, liên kết hệ thống xung quanh và migration dữ liệu. Hợp nhất dữ liệu phân mảnh theo phòng ban, tăng cường cả quyết định quản trị và vận hành hiện trường.",
        "features": [
            ("ERP導入・連携", "会計・販売・在庫・生産など基幹業務の統合"),
            ("CRM構築", "顧客管理、商談管理、マーケティング自動化"),
            ("カスタマイズ", "業種・業務フローに合わせた機能拡張"),
            ("データ連携", "既存システム・EC・BIとのシームレス連携"),
        ],
        "features_vi": [
            ("Triển khai·liên kết ERP", "Tích hợp kế toán·bán hàng·tồn kho·sản xuất…"),
            ("Xây dựng CRM", "Quản lý khách hàng, deal, tự động hóa marketing"),
            ("Custom", "Mở rộng chức năng theo ngành·quy trình"),
            ("Liên kết dữ liệu", "Liên kết mượt với hệ thống hiện có·EC·BI"),
        ],
        "process": [
            ("業務分析", "現行フローと課題の可視化"),
            ("要件定義", "標準機能とカスタム範囲の整理"),
            ("構築・移行", "設定、開発、データ移行"),
            ("トレーニング", "現場への定着支援"),
            ("運用改善", "活用度向上と追加改善"),
        ],
        "process_vi": [
            ("Phân tích nghiệp vụ", "Hình dung quy trình hiện tại và thách thức"),
            ("Định nghĩa yêu cầu", "Phân tách chức năng chuẩn và phạm vi custom"),
            ("Xây dựng·chuyển đổi", "Cấu hình, phát triển, migration dữ liệu"),
            ("Đào tạo", "Hỗ trợ gắn bó tại hiện trường"),
            ("Cải tiến vận hành", "Tăng mức sử dụng và cải tiến bổ sung"),
        ],
        "benefits": [
            "経営データのリアルタイム可視化",
            "部門横断の業務効率化",
            "顧客対応力と売上機会の最大化",
        ],
        "benefits_vi": [
            "Nhìn thấy dữ liệu quản trị theo thời gian thực",
            "Tối ưu nghiệp vụ xuyên phòng ban",
            "Tối đa hóa năng lực chăm sóc khách và cơ hội doanh thu",
        ],
    },
    {
        "slug": "cyber-security",
        "num": "08",
        "title": "サイバー・セキュリティ",
        "title_vi": "An ninh mạng",
        "en": "Cyber Security",
        "summary": "脅威から情報資産を守る、診断・対策・運用のセキュリティ支援",
        "summary_vi": "Hỗ trợ bảo mật — đánh giá·biện pháp·vận hành để bảo vệ tài sản thông tin",
        "image": "photo-network.jpg",
        "lead": "脆弱性診断、セキュリティ設計、監視、インシデント対応まで、多層防御の考え方で情報資産を保護します。開発段階からのセキュア設計と、運用フェーズの継続的な対策を両立します。",
        "lead_vi": "Bảo vệ tài sản thông tin theo tư duy phòng thủ nhiều lớp: đánh giá lỗ hổng, thiết kế bảo mật, giám sát, ứng phó sự cố. Kết hợp thiết kế bảo mật từ giai đoạn phát triển và biện pháp liên tục khi vận hành.",
        "features": [
            ("脆弱性診断", "Webアプリ・インフラ・クラウドのセキュリティ診断"),
            ("セキュア開発", "設計・実装段階でのセキュリティ要件組み込み"),
            ("監視・防御", "ログ監視、不正検知、アクセス制御の強化"),
            ("インシデント対応", "初動対応、原因分析、再発防止策の策定"),
        ],
        "features_vi": [
            ("Đánh giá lỗ hổng", "Đánh giá bảo mật Web app·hạ tầng·cloud"),
            ("Phát triển bảo mật", "Gắn yêu cầu bảo mật từ thiết kế·triển khai"),
            ("Giám sát·phòng thủ", "Theo dõi log, phát hiện bất thường, tăng cường kiểm soát truy cập"),
            ("Ứng phó sự cố", "Ứng phó ban đầu, phân tích nguyên nhân, ngăn tái diễn"),
        ],
        "process": [
            ("現状評価", "リスクと対策状況のアセスメント"),
            ("対策設計", "優先度に基づく改善ロードマップ"),
            ("実装", "技術対策・運用ルールの導入"),
            ("検証", "診断・ペネトレーションテスト"),
            ("継続運用", "監視・教育・定期見直し"),
        ],
        "process_vi": [
            ("Đánh giá hiện trạng", "Assessment rủi ro và biện pháp hiện có"),
            ("Thiết kế biện pháp", "Roadmap cải tiến theo mức ưu tiên"),
            ("Triển khai", "Áp dụng biện pháp kỹ thuật và quy tắc vận hành"),
            ("Kiểm chứng", "Đánh giá·penetration test"),
            ("Vận hành liên tục", "Giám sát·đào tạo·rà soát định kỳ"),
        ],
        "benefits": [
            "情報漏洩・サービス停止リスクの低減",
            "取引先・顧客からの信頼向上",
            "コンプライアンス要件への対応強化",
        ],
        "benefits_vi": [
            "Giảm rủi ro rò rỉ thông tin·gián đoạn dịch vụ",
            "Tăng niềm tin từ đối tác và khách hàng",
            "Tăng cường đáp ứng yêu cầu tuân thủ",
        ],
    },
]


def build_nav_links(active_file: str) -> tuple[str, str]:
    """Build main nav links and contact CTA (single contact entry)."""
    nav_parts = []
    for href, i18n_key, label in NAV_ITEMS:
        if href == "it-services.html":
            is_active = active_file in IT_SERVICE_PAGES
        else:
            is_active = href == active_file
        active_attr = " class='active'" if is_active else ""
        nav_parts.append(
            f'          <li><a href="{href}"{active_attr} data-i18n="{i18n_key}">{label}</a></li>'
        )
    nav_links = "\n".join(nav_parts)
    cta_active = " active" if active_file == "contact.html" else ""
    nav_cta = (
        f'                  <li class="nav-cta">'
        f'<a href="contact.html" class="btn-nav{cta_active}" data-i18n="nav.contact">お問い合わせ</a></li>'
    )
    return nav_links, nav_cta

FOOTER_HTML = dedent(
    """\
    <footer class="site-footer">
      <div class="container footer-grid">
        <div class="footer-brand">
          <img src="images/logo.png" alt="KATAO" class="footer-logo">
          <p><strong>株式会社カタオ総合</strong></p>
          <p class="footer-tagline" data-i18n="footer.tagline">機会を繋ぐ・未来を築く</p>
        </div>
        <div class="footer-col">
          <h4 data-i18n="footer.company">会社情報</h4>
          <ul>
            <li><a href="company.html" data-i18n="nav.company">会社概要</a></li>
            <li><a href="greeting.html" data-i18n="nav.greeting">代表者挨拶</a></li>
            <li><a href="business.html" data-i18n="nav.business">事業内容</a></li>
            <li><a href="jobs.html" data-i18n="nav.jobs">求人情報</a></li>
            <li><a href="news.html" data-i18n="nav.news">ニュース</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 data-i18n="footer.services">サービス</h4>
          <ul>
            <li><a href="it-services.html" data-i18n="footer.it">ITアウトソーシング</a></li>
            <li><a href="offshore-development.html" data-i18n="footer.offshore">オフショア開発</a></li>
            <li><a href="for-companies.html" data-i18n="footer.forCompanies">企業様へ</a></li>
            <li><a href="contact.html" data-i18n="footer.contactLink">お問い合わせ</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 data-i18n="footer.contact">お問い合わせ</h4>
          <address>〒123-0861<br>東京都足立区加賀１－７－５</address>
          <p>TEL: <a href="tel:0363362753">03-6336-2753</a></p>
          <p>Email: <a href="mailto:kataosogo.info@gmail.com">kataosogo.info@gmail.com</a></p>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="container">
          <p data-i18n="footer.copy">© 2026 株式会社カタオ総合 All Rights Reserved.</p>
        </div>
      </div>
    </footer>
    """
)


PAGE_TITLE_KEYS = {
    "index.html": "page.home",
    "company.html": "page.company",
    "greeting.html": "page.greeting",
    "business.html": "page.business",
    "it-services.html": "page.it",
    "offshore-development.html": "page.offshore-development",
    "application-development.html": "page.application-development",
    "migration.html": "page.migration",
    "maintenance-operations.html": "page.maintenance-operations",
    "cloud-computing.html": "page.cloud-computing",
    "ai-genai.html": "page.ai-genai",
    "erp-crm.html": "page.erp-crm",
    "cyber-security.html": "page.cyber-security",
    "for-companies.html": "page.forCompanies",
    "recruitment.html": "page.recruitment",
    "jobs.html": "page.jobs",
    "news.html": "page.news",
    "contact.html": "page.contact",
}


def _page_title_attr(active_file: str) -> str:
    key = PAGE_TITLE_KEYS.get(active_file)
    if not key:
        return ""
    return f' data-page-title="{key}"'


def _header_block(nav_links: str, nav_cta: str) -> str:
    return f"""\
          <header class="site-header">
            <div class="container header-inner">
              <a class="logo-link" href="index.html">
                <img src="images/logo.png" alt="株式会社カタオ総合 ロゴ">
                <span>株式会社カタオ総合</span>
              </a>
              <button class="nav-toggle" data-i18n-aria="nav.menu" aria-label="メニュー">☰</button>
              <nav class="main-nav" data-i18n-aria="nav.main" aria-label="メインナビゲーション">
                <ul>
        {nav_links}
        {nav_cta}
                  <li class="nav-lang">{LANG_SWITCH_HTML}
                  </li>
                </ul>
              </nav>
            </div>
          </header>"""


SCRIPTS_HTML = """\
          <script src="js/i18n-dict.js"></script>
          <script src="js/main.js"></script>
          <script src="js/i18n.js"></script>"""


def shell(title: str, active_file: str, body_html: str, hero_html: str = "") -> str:
    """Wrap a page body with shared header/nav/footer shell."""
    nav_links, nav_cta = build_nav_links(active_file)
    hero = f"\n{hero_html}\n" if hero_html else "\n"
    title_attr = _page_title_attr(active_file)
    header = _header_block(nav_links, nav_cta)

    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="ja"{title_attr}>
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
            <p class="loader-text" data-i18n="loader.text">読み込み中...</p>
          </div>
          <div class="page-transition"></div>
          <div class="scroll-progress"></div>

{header}{hero}
          <main class="site-main">
            <div class="container">
        {body_html}
            </div>
          </main>
        {FOOTER_HTML}
          <button class="back-to-top" data-i18n-aria="backToTop" aria-label="トップへ戻る">↑</button>
{SCRIPTS_HTML}
        </body>
        </html>
        """
    )


def page_hero(title: str, subtitle: str = "", title_key: str = "", sub_key: str = "") -> str:
    t_attr = f' data-i18n="{title_key}"' if title_key else ""
    if subtitle:
        s_attr = f' data-i18n="{sub_key}"' if sub_key else ""
        sub = f"<p{s_attr}>{subtitle}</p>"
    else:
        sub = ""
    return dedent(f"""\
    <section class="hero hero--compact">
      <div class="hero-overlay"></div>
      <div class="hero-content reveal">
        <h1{t_attr}>{title}</h1>
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
    header = _header_block(nav_links, nav_cta)

    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="ja" data-page-title="page.home">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta name="description" content="株式会社カタオ総合 — ベトナムと日本をつなぐ外国人人材紹介・登録支援機関" data-i18n-content="meta.homeDesc">
          <title>{title} | 株式会社カタオ総合</title>
          <link rel="stylesheet" href="css/style.css">
        </head>
        <body>
          <div class="page-loader">
            <div class="loader-spinner"></div>
            <img src="images/logo.png" alt="" class="loader-logo">
            <div class="loader-bar"><div class="loader-bar-fill"></div></div>
            <p class="loader-text" data-i18n="loader.text">読み込み中...</p>
          </div>
          <div class="page-transition"></div>
          <div class="scroll-progress"></div>

{header}
        {hero_html}
          <main class="site-main site-main--home">
        {body_html}
          </main>
        {FOOTER_HTML}
          <button class="back-to-top" data-i18n-aria="backToTop" aria-label="トップへ戻る">↑</button>
{SCRIPTS_HTML}
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
    header = _header_block(nav_links, nav_cta)
    title_attr = _page_title_attr(active_file)

    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="ja"{title_attr}>
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
            <p class="loader-text" data-i18n="loader.text">読み込み中...</p>
          </div>
          <div class="page-transition"></div>
          <div class="scroll-progress"></div>

{header}
        {content_html}
        {FOOTER_HTML}
          <button class="back-to-top" data-i18n-aria="backToTop" aria-label="トップへ戻る">↑</button>
{SCRIPTS_HTML}
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
        <span class="hero-badge" data-i18n="home.badge">外国人人材紹介事業</span>
        <h1 data-i18n="home.heroTitle">機会を繋ぐ・未来を築く</h1>
        <p data-i18n="home.heroLead">ベトナムと日本をつなぐ信頼のパートナー — 人材紹介から定着支援までワンストップ</p>
        <div class="hero-actions">
          <a href="for-companies.html" class="btn btn-primary" data-i18n="home.ctaCompanies">企業様はこちら</a>
          <a href="contact.html" class="btn btn-outline" data-i18n="home.ctaContact">お問い合わせ</a>
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
          <h2 data-i18n-html="home.aboutTitle">日本とベトナムをつなぐ<br>総合人材サービス</h2>
          <p data-i18n="home.aboutP1">株式会社カタオ総合は、革新的なソリューションを提供し、お客様の信頼に応えることを使命としています。ベトナムをはじめとする海外の教育機関・団体との強固なネットワークを活かし、日本語能力・専門スキル・勤労意識に優れた人材を厳選・育成し、日本企業へ紹介しております。</p>
          <p data-i18n="home.aboutP2">「信頼」「誠実」「挑戦」を企業理念とし、社会に貢献できる企業であり続けます。</p>
          <a href="company.html" class="btn btn-primary" data-i18n="home.aboutCta">会社概要を見る</a>
        </div>
        <div class="about-image reveal-right">
          <img src="images/photo-network.jpg" alt="国際人材紹介サービス">
        </div>
      </div>
    </section>

    <!-- Stats -->
    <section class="section-block section-stats">
      <div class="container stats-bar">
        <div class="stat reveal" data-delay="1"><span class="stat-num">2023</span><span class="stat-label" data-i18n="home.stat1">設立年</span></div>
        <div class="stat reveal" data-delay="2"><span class="stat-num">16</span><span class="stat-label" data-i18n="home.stat2">特定技能業種</span></div>
        <div class="stat reveal" data-delay="3"><span class="stat-num">7+</span><span class="stat-label" data-i18n="home.stat3">事業分野</span></div>
        <div class="stat reveal" data-delay="4"><span class="stat-num">100%</span><span class="stat-label" data-i18n="home.stat4">ワンストップ支援</span></div>
      </div>
    </section>

    <!-- Services -->
    <section class="section-block section-services">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-label">Services</span>
          <h2 data-i18n="home.servicesTitle">事業内容</h2>
          <p data-i18n="home.servicesLead">人材紹介からIT・建設DXまで、事業を幅広く展開</p>
        </div>
        <div class="services-grid">
          <a href="jobs.html" class="service-card service-card--live reveal" data-delay="1">
            <img src="images/photo-team.jpg" alt="求人情報サイト">
            <div class="service-card-body">
              <span class="service-badge service-badge--live" data-i18n="home.jobsBadge">公開中</span>
              <h3 data-i18n="home.jobsTitle">求人サービス</h3>
              <p data-i18n="home.jobsDesc">求職者と企業をつなぐ求人情報サイト。地域・給与での検索、履歴書からの求人提案、応募状況の確認まで。</p>
            </div>
          </a>
          <a href="business.html" class="service-card reveal" data-delay="2">
            <img src="images/photo-workplace.jpg" alt="技能実習・特定技能">
            <div class="service-card-body">
              <h3 data-i18n="home.svc1Title">技能実習・特定技能</h3>
              <p data-i18n="home.svc1Desc">育成・送出し、16業種対応の登録支援機関サービス</p>
            </div>
          </a>
          <a href="business.html" class="service-card reveal" data-delay="3">
            <img src="images/photo-team.jpg" alt="高度人材紹介">
            <div class="service-card-body">
              <h3 data-i18n="home.svc2Title">高度人材紹介</h3>
              <p data-i18n="home.svc2Desc">技術・人文知識・国際業務ビザ対応</p>
            </div>
          </a>
          <a href="business.html" class="service-card reveal" data-delay="4">
            <img src="images/photo-business.jpg" alt="生活・就業支援">
            <div class="service-card-body">
              <h3 data-i18n="home.svc3Title">生活・就業支援</h3>
              <p data-i18n="home.svc3Desc">ビザ、住居、日本語、定着支援のトータルサポート</p>
            </div>
          </a>
          <a href="business.html" class="service-card reveal" data-delay="5">
            <img src="images/photo-meeting.jpg" alt="通訳・翻訳・研修">
            <div class="service-card-body">
              <h3 data-i18n="home.svc4Title">通訳・翻訳・研修</h3>
              <p data-i18n="home.svc4Desc">言語サービスと教育コンサルティング</p>
            </div>
          </a>
          <a href="it-services.html" class="service-card reveal" data-delay="6">
            <img src="images/photo-office.jpg" alt="オフショア開発・ITアウトソーシング">
            <div class="service-card-body">
              <h3 data-i18n="home.svc6Title">ITアウトソーシング</h3>
              <p data-i18n="home.svc6Desc">オフショア開発、アプリ開発、クラウド、AI、セキュリティなど</p>
            </div>
          </a>
        </div>
        <div class="section-cta reveal" style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">
          <a href="jobs.html" class="btn btn-secondary" data-i18n="home.jobsFind">求人を探す</a>
          <a href="business.html" class="btn btn-primary" data-i18n="home.servicesCta">事業内容の詳細を見る</a>
        </div>
      </div>
    </section>

    <!-- Why Us -->
    <section class="section-block section-why">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-label">Why KATAO</span>
          <h2 data-i18n="home.whyTitle">カタオ総合が選ばれる理由</h2>
        </div>
        <div class="why-grid">
          <div class="why-card reveal" data-delay="1">
            <div class="why-icon">01</div>
            <h3 data-i18n="home.why1Title">ワンストップ対応</h3>
            <p data-i18n="home.why1Desc">人材選定から採用、入国後の生活・職場定着支援まで一貫したサービス</p>
          </div>
          <div class="why-card reveal" data-delay="2">
            <div class="why-icon">02</div>
            <h3 data-i18n="home.why2Title">ベトナム語サポート</h3>
            <p data-i18n="home.why2Desc">面接・生活指導・日常相談すべてベトナム語で対応可能</p>
          </div>
          <div class="why-card reveal" data-delay="3">
            <div class="why-icon">03</div>
            <h3 data-i18n="home.why3Title">法的手続き代行</h3>
            <p data-i18n="home.why3Desc">在留資格、ビザ発給、入国サポートまで全て代行</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Process -->
    <section class="section-block section-process">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-label">Process</span>
          <h2 data-i18n="home.processTitle">採用の流れ</h2>
          <p data-i18n="home.processLead">人材募集から就業開始まで5ステップで完全サポート</p>
        </div>
        <div class="steps">
          <div class="step reveal" data-delay="1"><div class="step-num">1</div><h4 data-i18n="home.step1Title">人材募集・紹介</h4><p data-i18n="home.step1Desc">ご要望をお伺いし最適な人材をご提案</p></div>
          <div class="step reveal" data-delay="2"><div class="step-num">2</div><h4 data-i18n="home.step2Title">面接対応</h4><p data-i18n="home.step2Desc">母国語スタッフが同行サポート</p></div>
          <div class="step reveal" data-delay="3"><div class="step-num">3</div><h4 data-i18n="home.step3Title">内定・書類申請</h4><p data-i18n="home.step3Desc">ビザ申請などトータルサポート</p></div>
          <div class="step reveal" data-delay="4"><div class="step-num">4</div><h4 data-i18n="home.step4Title">入国準備</h4><p data-i18n="home.step4Desc">生活環境整備を万全に</p></div>
          <div class="step reveal" data-delay="5"><div class="step-num">5</div><h4 data-i18n="home.step5Title">就業開始</h4><p data-i18n="home.step5Desc">定期的フォローアップ</p></div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="section-block section-cta-banner">
      <div class="container cta-inner reveal">
        <h2 data-i18n="home.ctaTitle">まずはお気軽にご相談ください</h2>
        <p data-i18n="home.ctaLead">貴社の人材課題に最適なソリューションをご提案いたします</p>
        <div class="hero-actions">
          <a href="contact.html" class="btn btn-white" data-i18n="home.ctaContact">お問い合わせ</a>
          <a href="for-companies.html" class="btn btn-outline-white" data-i18n="home.ctaForCompanies">企業様向け情報</a>
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
          <tr><th scope="row" data-i18n="company.labelName">会社名</th><td>株式会社カタオ総合</td></tr>
          <tr><th scope="row" data-i18n="company.labelAddress">本社所在地</th><td>〒123-0861 東京都足立区加賀１－７－５</td></tr>
          <tr><th scope="row" data-i18n="company.labelTel">電話番号</th><td>03-6336-2753</td></tr>
          <tr><th scope="row" data-i18n="company.labelEmail">メールアドレス</th><td><a href="mailto:kataosogo.info@gmail.com">kataosogo.info@gmail.com</a></td></tr>
          <tr><th scope="row" data-i18n="company.labelWeb">ホームページ</th><td><a href="https://kataosogo.jp/">https://kataosogo.jp</a></td></tr>
          <tr><th scope="row" data-i18n="company.labelFounded">設立年月日</th><td>2023年6月1日</td></tr>
          <tr><th scope="row" data-i18n="company.labelCapital">資本金</th><td>6,500,000円</td></tr>
          <tr><th scope="row" data-i18n="company.labelCeo">代表取締役</th><td>ファム・バン・カン</td></tr>
          <tr><th scope="row" data-i18n="company.labelLicenseJob">職業紹介 許可番号</th><td>13-ユ-315921</td></tr>
          <tr><th scope="row" data-i18n="company.labelLicenseSupport">登録支援機関許可番号</th><td>25登-012387</td></tr>
        </tbody>
      </table>
    </article>

    <section class="section">
      <div class="mission-block">
      <h2 data-i18n="company.missionTitle">使命（Mission）</h2>
      <p data-i18n="company.missionBody">ベトナムと日本をつなぐ架け橋として、人と企業、技術と文化を結び、双方の持続的な発展に貢献します。</p>
      </div>
    </section>

    <section class="section">
      <div class="mission-block">
      <h2 data-i18n="company.visionTitle">ビジョン（Vision）</h2>
      <p data-i18n="company.visionBody">信頼される国際パートナーとして、人材・貿易・教育の分野でアジアを代表する企業を目指します。</p>
      </div>
    </section>

    <section class="section">
      <div class="mission-block">
      <h2 data-i18n="company.policyTitle">企業方針（Policy）</h2>
      <p data-i18n="company.policyBody">誠実（Seijitsu）・信頼（Shinrai）・挑戦（Chousen）＝ 真心をもって信頼を築き、常に新たな挑戦を続ける。</p>
      </div>
    </section>

    <section class="section">
      <div class="mission-block">
      <h2 data-i18n="company.sloganTitle">スローガン（Slogan）</h2>
      <p data-i18n="company.sloganBody">人と企業をつなぎ、未来を創る。Connecting People and Companies, Creating the Future.</p>
      </div>
    </section>
    """
    write_page(
        "company.html",
        "会社概要",
        "company.html",
        body_html,
        page_hero("会社概要", "Company Profile", "company.heroTitle", "company.heroSub"),
    )


def build_greeting() -> None:
    body_html = """
    <article class="greeting-article">
      <div class="greeting-profile reveal">
        <img src="images/photo-hero.jpg" alt="代表取締役 ファム・バン・カン">
        <p class="greeting-name" data-i18n="greeting.name">代表取締役　ファム・バン・カン</p>
      </div>
      <div class="greeting-text">
      <p data-i18n="greeting.p1">はじめに、株式会社カタオ総合を代表いたしまして、お客様ならびにビジネスパートナーの皆様のご健康とご繁栄を心よりお祈り申し上げます。平素より格別のご高配を賜り、厚く御礼申し上げます。</p>
      <p data-i18n="greeting.p2">私はベトナムの建設大学（National University of Civil Engineering）を卒業後、約20年間にわたり日本で勤務し、建設業界を中心に幅広い経験を積んでまいりました。その中で、日本の高度な技術力と誠実な企業文化を学び、「日本とベトナムをつなぐ架け橋となりたい」という強い想いを抱くようになりました。</p>
      <p data-i18n="greeting.p3">現在、日本では少子高齢化が進み、若年層の人材不足が深刻な課題となっております。一方で、ベトナムには優秀で勤勉、かつ学ぶ意欲にあふれた若者が数多く存在します。こうした人材が日本で働き、技術や経験を学ぶことは、両国の発展と相互理解の促進につながるものと確信しております。</p>
      <p data-i18n="greeting.p4">この理念のもと、株式会社カタオ総合は、貿易・観光・投資、そして特に人材交流の分野において、日本とベトナムを結ぶ信頼のパートナーとして設立されました。「最高のサービスでお客様の信頼に応えること」を企業方針に掲げ、誠実・信頼・挑戦の精神で事業を展開してまいります。</p>
      <p data-i18n="greeting.p5">今後ともご指導ご鞭撻を賜りますようお願い申し上げます。皆様の変わらぬご支援とご愛顧を心よりお願い申し上げます。</p>
      </div>
    </article>
    """
    write_page(
        "greeting.html",
        "代表者挨拶",
        "greeting.html",
        body_html,
        page_hero("代表者挨拶", title_key="greeting.heroTitle"),
    )


def build_business() -> None:
    content_html = """<section class="hero hero--business">
  <img src="images/photo-office.jpg" alt="事業内容" class="hero-image">
  <div class="hero-overlay"></div>
  <div class="hero-content reveal">
    <span class="hero-badge">Business Fields</span>
    <h1 data-i18n="business.heroTitle">事業内容</h1>
    <p data-i18n="business.heroLead">人材紹介からオフショア開発まで、ワンストップでサポート</p>
  </div>
</section>

<main class="site-main site-main--business">

  <section class="section-block section-about">
    <div class="container about-split">
      <div class="about-text reveal-left">
        <span class="section-label">Overview</span>
        <h2 data-i18n="business.overviewTitle">国際人材紹介事業の概要</h2>
        <p data-i18n="business.overviewP1">当社は、日本国内の多様化する企業ニーズに応えるため、海外人材の紹介およびマッチング事業を展開しております。</p>
        <p data-i18n="business.overviewP2">ベトナムをはじめとする海外の教育機関や団体との強固なネットワークを活かし、日本語能力・専門スキル・勤労意識に優れた人材を厳選・育成し、日本企業へ紹介しています。</p>
        <p data-i18n="business.overviewP3">また、企業様の受入れに関する法的手続きの支援、人材管理、生活サポートなど、採用後のフォロー体制も充実させ、企業と人材双方の信頼関係構築に努めております。</p>
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
          <h2 data-i18n="business.supportTitle">国際人材の支援事業について</h2>
          <p data-i18n="business.supportLead">当社は、外国人材が日本で安心して働き、生活できるよう、入国前から就労後まで一貫したサポート体制を提供しております。</p>
          <div class="biz-support-grid">
            <div class="biz-support-item reveal" data-delay="1">
              <span class="biz-support-icon">01</span>
              <p data-i18n="business.support1">在留資格・ビザ申請、入国に関する手続き支援</p>
            </div>
            <div class="biz-support-item reveal" data-delay="2">
              <span class="biz-support-icon">02</span>
              <p data-i18n="business.support2">生活支援（住居・日本語学習・地域交流など）</p>
            </div>
            <div class="biz-support-item reveal" data-delay="3">
              <span class="biz-support-icon">03</span>
              <p data-i18n="business.support3">キャリア相談・職場定着・スキルアップ支援</p>
            </div>
            <div class="biz-support-item reveal" data-delay="4">
              <span class="biz-support-icon">04</span>
              <p data-i18n="business.support4">受入企業への管理・教育・文化理解のサポート</p>
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
        <h2 data-i18n="business.fieldsTitle">業務分野</h2>
        <p data-i18n="business.fieldsLead">7つの事業分野で、企業と人材の双方をトータルサポート</p>
      </div>
      <div class="biz-field-grid">
        <a href="#field-1" class="biz-field-card reveal" data-delay="1">
          <img src="images/photo-workplace.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">01</span><h3 data-i18n="business.field1Card">技能実習生・特定技能者の育成・送出し</h3></div>
        </a>
        <a href="#field-2" class="biz-field-card reveal" data-delay="2">
          <img src="images/photo-team.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">02</span><h3 data-i18n="business.field2Card">日本企業への人材紹介</h3></div>
        </a>
        <a href="#field-3" class="biz-field-card reveal" data-delay="3">
          <img src="images/photo-business.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">03</span><h3 data-i18n="business.field3Card">登録支援機関サービス</h3></div>
        </a>
        <a href="#field-4" class="biz-field-card reveal" data-delay="4">
          <img src="images/photo-meeting.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">04</span><h3 data-i18n="business.field4Card">通訳・翻訳・研修・教育コンサル</h3></div>
        </a>
        <a href="#field-5" class="biz-field-card reveal" data-delay="5">
          <img src="images/photo-network.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">05</span><h3 data-i18n="business.field5Card">国際連携・技術協力支援</h3></div>
        </a>
        <a href="#field-6" class="biz-field-card reveal" data-delay="6">
          <img src="images/photo-workplace.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">06</span><h3 data-i18n="business.field6Card">衣料品製造・卸売・小売</h3></div>
        </a>
        <a href="it-services.html" class="biz-field-card reveal" data-delay="7">
          <img src="images/photo-office.jpg" alt="">
          <div class="biz-field-card-body"><span class="biz-field-num">07</span><h3 data-i18n="business.field7Card">オフショア開発・ITアウトソーシング</h3></div>
        </a>
      </div>
    </div>
  </section>

  <section id="field-1" class="section-block">
    <div class="container biz-split">
      <div class="biz-content reveal-left">
        <span class="biz-field-num">01</span>
        <h2 data-i18n="business.field1Title">外国人技能実習生・特定技能者の育成および送出し事業</h2>
        <p data-i18n="business.field1P1">当社は、外国人技能実習生および特定技能者の育成・送出しを行っております。</p>
        <ul class="biz-feature-list">
          <li data-i18n="business.field1Li1">出国前の技能・日本語教育</li>
          <li data-i18n="business.field1Li2">法的手続き・在留資格の支援</li>
          <li data-i18n="business.field1Li3">実習・就労期間中のサポート</li>
          <li data-i18n="business.field1Li4">受入企業との連携・研修プログラム提供</li>
        </ul>
        <p data-i18n="business.field1P2">外国人材の技能・経験・適応能力の向上を促進し、企業に対して高品質な人材の提供を実現しています。</p>
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
        <h2 data-i18n="business.field2Title">日本企業への人材紹介事業</h2>
        <p data-i18n="business.field2P1">技術・人文知識・国際業務ビザ対応の人材紹介サービスを提供しております。</p>
        <ul class="biz-feature-list">
          <li data-i18n="business.field2Li1">技術（Engineering / 技術分野）</li>
          <li data-i18n="business.field2Li2">人文知識・国際業務（Humanities / International Business）</li>
          <li data-i18n="business.field2Li3">スキル・経験・日本語能力に適した人材の選定と紹介</li>
          <li data-i18n="business.field2Li4">在留資格取得支援・受入れ体制整備コンサルティング</li>
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
          <h2 data-i18n="business.field3Title">登録支援機関としての生活・就業支援サービス</h2>
          <p data-i18n="business.field3P1">「特定技能」は2019年4月に導入された在留資格で、人手不足が深刻な16業種で外国人労働者の受け入れが可能です。</p>
          <div class="industry-grid">
            <span class="industry-item" data-i18n="business.ind1">介護</span><span class="industry-item" data-i18n="business.ind2">ビルクリーニング</span>
            <span class="industry-item" data-i18n="business.ind3">工業製品製造業</span><span class="industry-item" data-i18n="business.ind4">建設</span>
            <span class="industry-item" data-i18n="business.ind5">造船・舶用工業</span><span class="industry-item" data-i18n="business.ind6">自動車整備</span>
            <span class="industry-item" data-i18n="business.ind7">航空</span><span class="industry-item" data-i18n="business.ind8">宿泊</span>
            <span class="industry-item" data-i18n="business.ind9">自動車運送業</span><span class="industry-item" data-i18n="business.ind10">鉄道</span>
            <span class="industry-item" data-i18n="business.ind11">農業</span><span class="industry-item" data-i18n="business.ind12">漁業</span>
            <span class="industry-item" data-i18n="business.ind13">飲食料品製造業</span><span class="industry-item" data-i18n="business.ind14">外食業</span>
            <span class="industry-item" data-i18n="business.ind15">林業</span><span class="industry-item" data-i18n="business.ind16">木材産業</span>
          </div>
          <h3 data-i18n="business.meritTitle">採用のメリット</h3>
          <div class="biz-benefit-grid">
            <div class="biz-benefit-card reveal" data-delay="1"><strong data-i18n="business.merit1Label">メリット 1</strong><span data-i18n="business.merit1">人材不足の解消</span></div>
            <div class="biz-benefit-card reveal" data-delay="2"><strong data-i18n="business.merit2Label">メリット 2</strong><span data-i18n="business.merit2">日本文化・日本語への理解</span></div>
            <div class="biz-benefit-card reveal" data-delay="3"><strong data-i18n="business.merit3Label">メリット 3</strong><span data-i18n="business.merit3">即戦力の採用</span></div>
          </div>
        </div>
      </div>

      <h3 class="reveal" style="text-align:center;margin-top:48px;color:var(--green-dark);" data-i18n="business.sswFlowTitle">特定技能 外国人採用の流れ</h3>
      <div class="biz-steps">
        <div class="biz-step reveal" data-delay="1"><div class="biz-step-num">1</div><h4 data-i18n="business.step1Title">人材募集・紹介</h4><p data-i18n="business.step1Desc">ご要望をお伺いし最適な人材をご提案</p></div>
        <div class="biz-step reveal" data-delay="2"><div class="biz-step-num">2</div><h4 data-i18n="business.step2Title">面接対応</h4><p data-i18n="business.step2Desc">母国語スタッフが同行サポート</p></div>
        <div class="biz-step reveal" data-delay="3"><div class="biz-step-num">3</div><h4 data-i18n="business.step3Title">内定・書類申請</h4><p data-i18n="business.step3Desc">ビザ申請などトータルサポート</p></div>
        <div class="biz-step reveal" data-delay="4"><div class="biz-step-num">4</div><h4 data-i18n="business.step4Title">入国準備</h4><p data-i18n="business.step4Desc">生活環境整備を万全に</p></div>
        <div class="biz-step reveal" data-delay="5"><div class="biz-step-num">5</div><h4 data-i18n="business.step5Title">就業開始</h4><p data-i18n="business.step5Desc">定期的フォローアップ</p></div>
      </div>

      <div class="biz-point-grid">
        <div class="biz-point-card reveal" data-delay="1">
          <h4 data-i18n="business.point1Title">POINT 1 – ワンストップ対応</h4>
          <p data-i18n="business.point1Body">人材選定から定着支援まで一貫したサービスを提供。即戦力となるベトナム人材を手間なく採用できます。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="2">
          <h4 data-i18n="business.point2Title">POINT 2 – ベトナム語サポート</h4>
          <p data-i18n="business.point2Body">面接・生活指導・日常相談など、すべてベトナム語で対応可能な専門スタッフが常駐しています。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="3">
          <h4 data-i18n="business.point3Title">POINT 3 – 法的手続き代行</h4>
          <p data-i18n="business.point3Body">特定技能・技術・人文知識・国際業務に関する全ての書類手続きを代行いたします。</p>
        </div>
      </div>
    </div>
  </section>

  <section id="field-4" class="section-block">
    <div class="container biz-split">
      <div class="biz-content reveal-left">
        <span class="biz-field-num">04</span>
        <h2 data-i18n="business.field4Title">通訳・翻訳・研修・教育コンサルティング事業</h2>
        <p data-i18n="business.field4P1">言語および教育分野における包括的なサービスを提供しております。</p>
        <ul class="biz-feature-list">
          <li data-i18n="business.field4Li1">通訳サービス：会議、研修、国際イベントでのコミュニケーション支援</li>
          <li data-i18n="business.field4Li2">翻訳サービス：専門文書、契約書、マニュアル等の正確な翻訳</li>
          <li data-i18n="business.field4Li3">研修事業：スキル研修、日本語教育、業務研修の実施</li>
          <li data-i18n="business.field4Li4">教育コンサルティング：人材育成・スキル開発のアドバイス</li>
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
        <h2 data-i18n="business.field5Title">ベトナム企業・団体との国際連携および技術協力支援</h2>
        <p data-i18n="business.field5P1">日本とベトナム両国間における企業・団体・協会などとの国際的な連携および技術協力の促進を目的として活動しています。</p>
        <p data-i18n="business.field5P2">技術移転、人材育成、投資・生産分野での連携プロジェクトを支援し、建設業、機械産業、農業、人材開発などさまざまな分野での協力を推進してまいります。</p>
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
        <h2 data-i18n="business.field6Title">衣料品製造・卸売・小売事業</h2>
        <p data-i18n="business.field6P1">ベトナムおよび中国で製造された衣料品の卸売・小売を行い、日本市場向けに提供しております。</p>
        <ul class="biz-feature-list">
          <li data-i18n-html="business.field6Li1Html"><strong>高品質・トレンド重視</strong> — 品質管理徹底、最新トレンド対応</li>
          <li data-i18n-html="business.field6Li2Html"><strong>卸売・小売両対応</strong> — 店舗・オンライン・業者向け卸売</li>
          <li data-i18n-html="business.field6Li3Html"><strong>日本市場に最適化</strong> — サイズ感・デザインに合わせた商品選定</li>
          <li data-i18n-html="business.field6Li4Html"><strong>将来的な展望</strong> — 全国の消費者へ販売拡大</li>
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
        <h2 data-i18n="business.field7Title">オフショア開発・ITアウトソーシング</h2>
        <p data-i18n="business.field7P1">ベトナムの優秀なITエンジニアと日本企業をつなぎ、日本市場のニーズに合わせたソフトウェア開発およびITアウトソーシングを提供しております。</p>
        <ul class="biz-feature-list">
          <li data-i18n-html="business.field7Li1Html"><strong>オフショア開発</strong> — 日本品質×合理コストで、要件定義から保守まで一貫対応</li>
          <li data-i18n-html="business.field7Li2Html"><strong>アプリケーション開発</strong> — Web・モバイル・業務システムの設計・実装</li>
          <li data-i18n-html="business.field7Li3Html"><strong>移行／クラウド／AI</strong> — レガシー刷新、クラウド活用、生成AI導入を支援</li>
          <li data-i18n-html="business.field7Li4Html"><strong>ERP・CRM／セキュリティ</strong> — 基幹・顧客管理とサイバーセキュリティ対策</li>
        </ul>
        <p data-i18n="business.field7P2">お客様のDX推進・業務効率化・新規サービス創出を力強くサポートいたします。</p>
        <a href="it-services.html" class="btn btn-primary" style="margin-top:20px;" data-i18n="business.field7Cta">ITサービスの詳細を見る</a>
      </div>
      <div class="biz-image reveal-left">
        <img src="images/photo-team.jpg" alt="オフショア開発チーム">
      </div>
    </div>
  </section>

  <section class="section-block section-cta-banner">
    <div class="container cta-inner reveal">
      <h2 data-i18n="business.ctaTitle">事業に関するご相談はこちら</h2>
      <p data-i18n="business.ctaLead">貴社のニーズに最適なサービスをご提案いたします</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-white" data-i18n="business.ctaContact">お問い合わせ</a>
        <a href="for-companies.html" class="btn btn-outline-white" data-i18n="business.ctaForCompanies">企業様向け情報</a>
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
    <h1 data-i18n="forCompanies.heroTitle">企業様へ</h1>
    <p data-i18n="forCompanies.heroLead">ベトナム人材と日本企業をつなぐ、信頼のパートナー</p>
  </div>
</section>

<main class="site-main site-main--business">

  <section class="section-block section-about">
    <div class="container about-split">
      <div class="about-text reveal-left">
        <span class="section-label">For Companies</span>
        <h2 data-i18n-html="forCompanies.introTitle">日本企業の成長を支援する<br>外国人材紹介サービス</h2>
        <p data-i18n="forCompanies.introP1">私たちの会社は、革新的な外国人材紹介サービスを通じて、日本企業の成長を支援しております。多様な文化やスキルを持つ人材を企業のニーズに合わせてマッチングすることで、国際的な競争力を高め、新たな可能性を創出します。</p>
        <p data-i18n="forCompanies.introP2">ぜひ、私たちと共に未来を切り開いていきましょう。</p>
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
        <h2 data-i18n="forCompanies.talentTitle">ご紹介可能な人材</h2>
        <p data-i18n="forCompanies.talentLead">技能実習生から高度人材まで、企業のニーズに合わせた人材をご提案</p>
      </div>
      <div class="biz-field-grid">
        <div class="biz-field-card reveal" data-delay="1">
          <img src="images/photo-workplace.jpg" alt="技能実習生">
          <div class="biz-field-card-body">
            <span class="biz-field-num">01</span>
            <h3 data-i18n="forCompanies.talent1Title">技能実習生</h3>
            <p data-i18n="forCompanies.talent1Desc">事前教育を経て、日本の現場で技能を習得・活躍する人材</p>
          </div>
        </div>
        <div class="biz-field-card reveal" data-delay="2">
          <img src="images/photo-business.jpg" alt="特定技能者">
          <div class="biz-field-card-body">
            <span class="biz-field-num">02</span>
            <h3 data-i18n="forCompanies.talent2Title">特定技能者</h3>
            <p data-i18n="forCompanies.talent2Desc">16業種で即戦力として活躍できる特定技能在留資格の人材</p>
          </div>
        </div>
        <div class="biz-field-card reveal" data-delay="3">
          <img src="images/photo-team.jpg" alt="高度人材">
          <div class="biz-field-card-body">
            <span class="biz-field-num">03</span>
            <h3 data-i18n="forCompanies.talent3Title">高度人材・技術者・専門家</h3>
            <p data-i18n="forCompanies.talent3Desc">技術・人文知識・国際業務ビザ対応の専門スキル人材</p>
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
        <h2 data-i18n="forCompanies.bridgeTitle">ベトナム人材と日本企業をつなぐ架け橋</h2>
        <p data-i18n="forCompanies.bridgeLead">当社は、ベトナム人材の日本企業への紹介サービスを専門に提供しております。企業様向けに以下のサポートを提供しております。</p>
        <ul class="biz-feature-list">
          <li data-i18n="forCompanies.bridgeLi1">人材選定・マッチング</li>
          <li data-i18n="forCompanies.bridgeLi2">研修・教育プログラムの提供</li>
          <li data-i18n="forCompanies.bridgeLi3">法的手続きおよび在留資格（ビザ）取得支援</li>
          <li data-i18n="forCompanies.bridgeLi4">受入れ後の人材管理・フォローアップ</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container biz-split biz-split--reverse">
      <div class="biz-content reveal-right">
        <span class="section-label">Talent Care</span>
        <h2 data-i18n="forCompanies.careTitle">人材への育成・定着支援</h2>
        <p data-i18n="forCompanies.careLead">ベトナム人材には日本語教育・専門スキル研修・生活指導を行い、日本での職場適応力向上と長期的なキャリア成長をサポートしております。</p>
        <div class="biz-support-grid">
          <div class="biz-support-item reveal" data-delay="1">
            <span class="biz-support-icon">01</span>
            <p data-i18n="forCompanies.care1">日本語教育・コミュニケーション研修</p>
          </div>
          <div class="biz-support-item reveal" data-delay="2">
            <span class="biz-support-icon">02</span>
            <p data-i18n="forCompanies.care2">専門スキル・業務研修プログラム</p>
          </div>
          <div class="biz-support-item reveal" data-delay="3">
            <span class="biz-support-icon">03</span>
            <p data-i18n="forCompanies.care3">生活指導・文化適応サポート</p>
          </div>
          <div class="biz-support-item reveal" data-delay="4">
            <span class="biz-support-icon">04</span>
            <p data-i18n="forCompanies.care4">キャリア相談・長期成長支援</p>
          </div>
        </div>
        <p data-i18n="forCompanies.careClose">ベトナム・日本における広範なネットワークを活用し、企業様には質の高い人材の提供、人材には安心して働ける環境とキャリア形成の機会を提供いたします。</p>
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
        <h2 data-i18n="forCompanies.whyTitle">カタオ総合が選ばれる理由</h2>
      </div>
      <div class="biz-point-grid">
        <div class="biz-point-card reveal" data-delay="1">
          <h4 data-i18n="forCompanies.why1Title">ワンストップ対応</h4>
          <p data-i18n="forCompanies.why1Body">人材選定から採用、入国後の生活・職場定着支援まで一貫したサービス。企業様は手間なく即戦力人材を採用できます。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="2">
          <h4 data-i18n="forCompanies.why2Title">ベトナム語ネイティブサポート</h4>
          <p data-i18n="forCompanies.why2Body">面接・生活指導・日常相談など、すべてベトナム語で対応可能。スムーズなコミュニケーションを実現します。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="3">
          <h4 data-i18n="forCompanies.why3Title">法的手続きのトータル代行</h4>
          <p data-i18n="forCompanies.why3Body">在留資格・ビザ申請から入国サポートまで、外国人雇用に必要な手続きをすべて代行いたします。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-label">Process</span>
        <h2 data-i18n="forCompanies.processTitle">採用の流れ</h2>
        <p data-i18n="forCompanies.processLead">人材募集から就業開始まで5ステップで完全サポート</p>
      </div>
      <div class="biz-steps">
        <div class="biz-step reveal" data-delay="1"><div class="biz-step-num">1</div><h4 data-i18n="forCompanies.step1Title">人材募集・紹介</h4><p data-i18n="forCompanies.step1Desc">ご要望をお伺いし最適な人材をご提案</p></div>
        <div class="biz-step reveal" data-delay="2"><div class="biz-step-num">2</div><h4 data-i18n="forCompanies.step2Title">面接対応</h4><p data-i18n="forCompanies.step2Desc">母国語スタッフが同行サポート</p></div>
        <div class="biz-step reveal" data-delay="3"><div class="biz-step-num">3</div><h4 data-i18n="forCompanies.step3Title">内定・書類申請</h4><p data-i18n="forCompanies.step3Desc">ビザ申請などトータルサポート</p></div>
        <div class="biz-step reveal" data-delay="4"><div class="biz-step-num">4</div><h4 data-i18n="forCompanies.step4Title">入国準備</h4><p data-i18n="forCompanies.step4Desc">生活環境整備を万全に</p></div>
        <div class="biz-step reveal" data-delay="5"><div class="biz-step-num">5</div><h4 data-i18n="forCompanies.step5Title">就業開始</h4><p data-i18n="forCompanies.step5Desc">定期的フォローアップ</p></div>
      </div>
    </div>
  </section>

  <section class="section-block section-cta-banner">
    <div class="container cta-inner reveal">
      <h2 data-i18n="forCompanies.ctaTitle">まずはお気軽にご相談ください</h2>
      <p data-i18n="forCompanies.ctaLead">貴社の人材課題に最適なソリューションをご提案いたします</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-white" data-i18n="forCompanies.ctaContact">お問い合わせ</a>
        <a href="business.html" class="btn btn-outline-white" data-i18n="forCompanies.ctaBusiness">事業内容を見る</a>
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
    <h1 data-i18n="recruitment.heroTitle">採用情報</h1>
    <p data-i18n="recruitment.heroLead">国際人材の架け橋として、共に未来を築きませんか</p>
  </div>
</section>

<main class="site-main site-main--business">

  <section class="section-block section-about">
    <div class="container about-split">
      <div class="about-text reveal-left">
        <span class="section-label">Join Us</span>
        <h2 data-i18n-html="recruitment.introTitle">株式会社カタオ総合で<br>一緒に働きませんか？</h2>
        <p data-i18n="recruitment.introP1">私たち株式会社カタオ総合は、ベトナム人材の育成・紹介、外国人技能実習生・特定技能者のサポート、通訳・翻訳・教育コンサルティングなど、多岐にわたる事業を展開しています。</p>
        <p data-i18n="recruitment.introP2">国際的な視点を持ち、日本企業と海外人材の架け橋となるやりがいのある仕事に挑戦しませんか？</p>
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
        <h2 data-i18n="recruitment.positionsTitle">募集職種</h2>
        <p data-i18n="recruitment.positionsLead">あなたのスキルと経験を活かせるポジションをご用意しています</p>
      </div>
      <div class="recruit-job-grid">
        <div class="recruit-job-card reveal" data-delay="1">
          <img src="images/photo-meeting.jpg" alt="人材コーディネーター">
          <div class="recruit-job-body">
            <span class="biz-field-num">01</span>
            <h3 data-i18n="recruitment.job1Title">人材コーディネーター / キャリアアドバイザー</h3>
            <ul>
              <li data-i18n="recruitment.job1Li1">外国人材の採用・紹介・フォローアップ業務</li>
              <li data-i18n="recruitment.job1Li2">日本企業と外国人材のマッチングサポート</li>
              <li data-i18n="recruitment.job1Li3">日本語・ベトナム語対応可能な方歓迎</li>
            </ul>
          </div>
        </div>
        <div class="recruit-job-card reveal" data-delay="2">
          <img src="images/photo-business.jpg" alt="通訳・翻訳スタッフ">
          <div class="recruit-job-body">
            <span class="biz-field-num">02</span>
            <h3 data-i18n="recruitment.job2Title">通訳・翻訳スタッフ</h3>
            <ul>
              <li data-i18n="recruitment.job2Li1">会議、研修、契約書類などの通訳・翻訳業務</li>
              <li data-i18n="recruitment.job2Li2">日本語とベトナム語に精通した方</li>
            </ul>
          </div>
        </div>
        <div class="recruit-job-card reveal" data-delay="3">
          <img src="images/photo-office.jpg" alt="事務・総務スタッフ">
          <div class="recruit-job-body">
            <span class="biz-field-num">03</span>
            <h3 data-i18n="recruitment.job3Title">事務・総務スタッフ</h3>
            <ul>
              <li data-i18n="recruitment.job3Li1">採用・入国手続きサポート</li>
              <li data-i18n="recruitment.job3Li2">書類作成、社内管理業務</li>
            </ul>
          </div>
        </div>
        <div class="recruit-job-card reveal" data-delay="4">
          <img src="images/photo-network.jpg" alt="営業・営業企画">
          <div class="recruit-job-body">
            <span class="biz-field-num">04</span>
            <h3 data-i18n="recruitment.job4Title">営業・営業企画</h3>
            <ul>
              <li data-i18n="recruitment.job4Li1">日本企業向け人材提案・衣料品販売</li>
              <li data-i18n="recruitment.job4Li2">市場調査、販路開拓</li>
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
        <h2 data-i18n="recruitment.idealTitle">求める人物像</h2>
      </div>
      <div class="biz-benefit-grid biz-benefit-grid--4">
        <div class="biz-benefit-card reveal" data-delay="1"><strong data-i18n="recruitment.ideal1Label">グローバル視点</strong><span data-i18n="recruitment.ideal1">チームで協力できる方</span></div>
        <div class="biz-benefit-card reveal" data-delay="2"><strong data-i18n="recruitment.ideal2Label">挑戦意欲</strong><span data-i18n="recruitment.ideal2">新しいことに挑戦する意欲がある方</span></div>
        <div class="biz-benefit-card reveal" data-delay="3"><strong data-i18n="recruitment.ideal3Label">語学力</strong><span data-i18n="recruitment.ideal3">日本語・ベトナム語を活用できる方</span></div>
        <div class="biz-benefit-card reveal" data-delay="4"><strong data-i18n="recruitment.ideal4Label">情熱</strong><span data-i18n="recruitment.ideal4">国際交流や人材育成に興味がある方</span></div>
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container biz-split">
      <div class="biz-content reveal-left">
        <span class="section-label">Conditions</span>
        <h2 data-i18n="recruitment.conditionsTitle">勤務条件</h2>
        <div class="recruit-conditions">
          <div class="recruit-condition-item reveal" data-delay="1">
            <span class="recruit-condition-label" data-i18n="recruitment.labelPlace">勤務地</span>
            <span class="recruit-condition-value">東京都足立区加賀1-7-5</span>
          </div>
          <div class="recruit-condition-item reveal" data-delay="2">
            <span class="recruit-condition-label" data-i18n="recruitment.labelHours">勤務時間</span>
            <span class="recruit-condition-value" data-i18n="recruitment.valueHours">9:00〜18:00（フレックスタイム応相談）</span>
          </div>
          <div class="recruit-condition-item reveal" data-delay="3">
            <span class="recruit-condition-label" data-i18n="recruitment.labelSalary">給与</span>
            <span class="recruit-condition-value" data-i18n="recruitment.valueSalary">経験・能力を考慮の上、当社規定により優遇</span>
          </div>
          <div class="recruit-condition-item reveal" data-delay="4">
            <span class="recruit-condition-label" data-i18n="recruitment.labelHoliday">休日休暇</span>
            <span class="recruit-condition-value" data-i18n="recruitment.valueHoliday">土日祝日、年末年始、有給休暇</span>
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
        <h2 data-i18n="recruitment.applyTitle">応募方法</h2>
        <p data-i18n="recruitment.applyLead">下記の書類をメールまたは郵送にてお送りください。</p>
        <ul class="biz-feature-list">
          <li data-i18n="recruitment.applyLi1">履歴書（写真貼付）</li>
          <li data-i18n="recruitment.applyLi2">職務経歴書（任意）</li>
        </ul>
        <div class="recruit-apply-contact">
          <span class="contact-label" data-i18n="recruitment.applyEmailLabel">応募先メール</span>
          <a href="mailto:kataosogo.info@gmail.com" class="contact-value">kataosogo.info@gmail.com</a>
          <p class="recruit-apply-note" data-i18n-html="recruitment.applyNoteHtml">件名：<strong>採用応募（氏名）</strong></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-block">
    <div class="container biz-split biz-split--reverse">
      <div class="biz-content reveal-right">
        <span class="section-label">Message</span>
        <h2 data-i18n="recruitment.messageTitle">私たちからのメッセージ</h2>
        <p data-i18n="recruitment.messageP1">私たちは、社員一人ひとりの成長を支え、挑戦する環境を提供しています。国際人材・人材育成・教育・販売など、多彩な事業に携わることで、キャリアの幅を広げることができます。</p>
        <p data-i18n="recruitment.messageP2">あなたの力を、株式会社カタオ総合で発揮してください。</p>
      </div>
      <div class="biz-image reveal-left">
        <img src="images/photo-meeting.jpg" alt="チームメッセージ">
      </div>
    </div>
  </section>

  <section class="section-block section-cta-banner">
    <div class="container cta-inner reveal">
      <h2 data-i18n="recruitment.ctaTitle">ご応募お待ちしております</h2>
      <p data-i18n="recruitment.ctaLead">ご質問がある方もお気軽にお問い合わせください</p>
      <div class="hero-actions">
        <a href="mailto:kataosogo.info@gmail.com" class="btn btn-white" data-i18n="recruitment.ctaMail">メールで応募</a>
        <a href="contact.html" class="btn btn-outline-white" data-i18n="recruitment.ctaContact">お問い合わせ</a>
      </div>
    </div>
  </section>

</main>"""
    write_fullwidth_page("recruitment.html", "採用情報", "recruitment.html", content_html)

def build_jobs() -> None:
    body_html = """
    <article class="section">
      <div class="job-card">
        <span class="service-badge service-badge--live" data-i18n="home.jobsBadge">公開中</span>
        <h2 data-i18n="jobs.siteTitle">求人情報サイト</h2>
        <p data-i18n="jobs.siteDesc">株式会社カタオ総合の求人サービスです。求職者と企業をつなぎ、地域・給与での検索、履歴書からの求人提案、応募状況の確認までを一つのサイトで提供します。特定技能・技術人文知識国際業務など、日本で働く方向けの求人を掲載しています。</p>
        <p style="margin-top:16px;"><a href="https://jobs.kataosogo.jp/" class="btn btn-primary" target="_blank" rel="noopener noreferrer" data-i18n="jobs.openSite">求人サイトを開く</a></p>
      </div>
      <div class="job-card">
        <h2 data-i18n="jobs.engTitle">技術・人文知識・国際業務ビザ人材（Engineer / Specialist）</h2>
        <p data-i18n="jobs.engDesc">専門知識と実務経験を活かし、日本企業での中長期的なキャリア形成を目指す方向けの求人カテゴリです。</p>
      </div>
      <div class="job-card">
        <h2 data-i18n="jobs.sswTitle">特定技能者（Specified Skilled Worker）</h2>
        <p data-i18n="jobs.sswDesc">特定技能制度の対象分野で、即戦力として活躍したい方向けの求人カテゴリです。</p>
      </div>
    </article>
    """
    write_page(
        "jobs.html",
        "求人情報",
        "jobs.html",
        body_html,
        page_hero("求人情報", "Job Openings", "jobs.heroTitle", "jobs.heroSub"),
    )


def build_news() -> None:
    body_html = """
    <article class="section news-list">
      <div class="news-card job-card">
        <div class="news-card-meta">
          <span class="service-badge service-badge--live" data-i18n="news.item1.badge">お知らせ</span>
          <time class="news-date" datetime="2026-09-10" data-i18n="news.item1.date">2026年9月10日</time>
        </div>
        <h2 data-i18n="news.item1.title">求人サイト jobs.kataosogo.jp を公開しました</h2>
        <p data-i18n="news.item1.body">株式会社カタオ総合は、求人情報サイト「jobs.kataosogo.jp」を公開いたしました。求職者の方は、希望の地域・職種・給与条件などから自分に合った求人を検索できます。また、コミュニティ・パートナー（協力者）の方も、候補者に適した求人を探し、マッチングを進めることができます。特定技能・技術人文知識国際業務など、日本で働く方向けの求人情報を掲載しております。ぜひご活用ください。</p>
        <div class="news-card-actions" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:16px;">
          <a href="https://jobs.kataosogo.jp/" class="btn btn-primary" target="_blank" rel="noopener noreferrer" data-i18n="news.item1.cta">求人サイトを開く</a>
          <a href="jobs.html" class="btn btn-secondary" data-i18n="news.item1.more">求人情報ページを見る</a>
        </div>
      </div>
    </article>
    """
    write_page(
        "news.html",
        "ニュース",
        "news.html",
        body_html,
        page_hero("ニュース", "News", "news.heroTitle", "news.heroSub"),
    )


def build_contact() -> None:
    body_html = """
    <article class="section contact-page">
      <h1 data-i18n="contact.title">お問い合わせ</h1>
      <div class="contact-form-embed">
        <iframe
          src="https://docs.google.com/forms/d/e/1FAIpQLSewFLz8l4xR8TXqAK_gY-Bl-48kcv4PWnbDzju2Lo9W5EwYnQ/viewform?embedded=true"
          width="640"
          height="800"
          frameborder="0"
          marginheight="0"
          marginwidth="0"
          data-i18n-aria="contact.iframeTitle"
          title="お問い合わせフォーム">
          <span data-i18n="contact.iframeFallback">処理中...</span>
        </iframe>
      </div>
    </article>
    """
    write_page("contact.html", "お問い合わせ", "contact.html", body_html)


def _it_key(slug: str, part: str) -> str:
    return f"itSvc.{slug}.{part}"


def _it_service_cards_html(exclude_slug=None) -> str:
    cards = []
    for i, svc in enumerate(IT_SERVICES, start=1):
        if exclude_slug and svc["slug"] == exclude_slug:
            continue
        slug = svc["slug"]
        cards.append(
            f"""        <a href="{slug}.html" class="biz-field-card reveal" data-delay="{(i % 4) + 1}">
          <img src="images/{svc['image']}" alt="{svc['title']}">
          <div class="biz-field-card-body">
            <span class="biz-field-num">{svc['num']}</span>
            <h3 data-i18n="{_it_key(slug, 'title')}">{svc['title']}</h3>
            <p data-i18n="{_it_key(slug, 'summary')}">{svc['summary']}</p>
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
    <h1 data-i18n="it.heroTitle">ITアウトソーシング</h1>
    <p data-i18n="it.heroLead">オフショア開発からAI・セキュリティまで、DXをトータル支援</p>
  </div>
</section>

<main class="site-main site-main--business">

  <section class="section-block section-about">
    <div class="container about-split">
      <div class="about-text reveal-left">
        <span class="section-label">Overview</span>
        <h2 data-i18n-html="it.overviewTitle">日本品質のITを、<br>合理的なコストで</h2>
        <p data-i18n="it.overviewP1">株式会社カタオ総合は、ベトナムの優秀なエンジニアリングリソースと日本側のブリッジ体制を組み合わせ、企業のDX・システム開発・運用課題を解決します。</p>
        <p data-i18n="it.overviewP2">アプリケーション開発、システム移行、クラウド、AI／生成AI、ERP・CRM、サイバーセキュリティまで、要件定義から保守運用までワンストップでご支援します。</p>
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
        <h2 data-i18n="it.servicesTitle">提供サービス</h2>
        <p data-i18n="it.servicesLead">8つのITサービスで、企画から運用までをトータルサポート</p>
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
        <h2 data-i18n="it.whyTitle">選ばれる理由</h2>
      </div>
      <div class="biz-point-grid">
        <div class="biz-point-card reveal" data-delay="1">
          <h4 data-i18n="it.why1Title">POINT 1 – ブリッジSE体制</h4>
          <p data-i18n="it.why1Body">日本語・ベトナム語・英語での丁寧なコミュニケーションにより、要件の齟齬を最小化します。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="2">
          <h4 data-i18n="it.why2Title">POINT 2 – 日本品質×コスト効率</h4>
          <p data-i18n="it.why2Body">レビュー・テスト・納品基準を日本水準で運用しつつ、オフショアのコストメリットを活かします。</p>
        </div>
        <div class="biz-point-card reveal" data-delay="3">
          <h4 data-i18n="it.why3Title">POINT 3 – 一気通貫サポート</h4>
          <p data-i18n="it.why3Body">開発だけでなく、移行・クラウド・AI・保守運用・セキュリティまで継続的に伴走します。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-block section-cta-banner">
    <div class="container cta-inner reveal">
      <h2 data-i18n="it.ctaTitle">ITアウトソーシングのご相談</h2>
      <p data-i18n="it.ctaLead">貴社の課題に最適なサービスをご提案いたします</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-white" data-i18n="it.ctaContact">お問い合わせ</a>
        <a href="business.html" class="btn btn-outline-white" data-i18n="it.ctaBusiness">事業内容を見る</a>
      </div>
    </div>
  </section>

</main>"""
    write_fullwidth_page("it-services.html", "ITアウトソーシング", "it-services.html", content_html)


def build_it_service_details() -> None:
    for svc in IT_SERVICES:
        slug = svc["slug"]
        features_html = "\n".join(
            f'          <li><strong data-i18n="{_it_key(slug, f"feat{i}Title")}">{title}</strong> — '
            f'<span data-i18n="{_it_key(slug, f"feat{i}Desc")}">{desc}</span></li>'
            for i, (title, desc) in enumerate(svc["features"], start=1)
        )
        process_html = "\n".join(
            f'        <div class="biz-step reveal" data-delay="{i}"><div class="biz-step-num">{i}</div>'
            f'<h4 data-i18n="{_it_key(slug, f"proc{i}Title")}">{title}</h4>'
            f'<p data-i18n="{_it_key(slug, f"proc{i}Desc")}">{desc}</p></div>'
            for i, (title, desc) in enumerate(svc["process"], start=1)
        )
        benefits_html = "\n".join(
            f'          <div class="biz-benefit-card reveal" data-delay="{i}">'
            f'<strong data-i18n="it.detail.merit{i}">メリット {i}</strong>'
            f'<span data-i18n="{_it_key(slug, f"benefit{i}")}">{b}</span></div>'
            for i, b in enumerate(svc["benefits"], start=1)
        )
        related = _it_service_cards_html(exclude_slug=slug)

        content_html = f"""<section class="hero hero--business">
  <img src="images/{svc['image']}" alt="{svc['title']}" class="hero-image">
  <div class="hero-overlay"></div>
  <div class="hero-content reveal">
    <span class="hero-badge">{svc['en']}</span>
    <h1 data-i18n="{_it_key(slug, 'title')}">{svc['title']}</h1>
    <p data-i18n="{_it_key(slug, 'summary')}">{svc['summary']}</p>
  </div>
</section>

<main class="site-main site-main--business">

  <section class="section-block">
    <div class="container">
      <nav class="breadcrumb reveal" data-i18n-aria="it.detail.breadcrumbAria" aria-label="パンくず">
        <a href="index.html" data-i18n="nav.home">ホーム</a>
        <span>/</span>
        <a href="it-services.html" data-i18n="it.heroTitle">ITアウトソーシング</a>
        <span>/</span>
        <span data-i18n="{_it_key(slug, 'title')}">{svc['title']}</span>
      </nav>
    </div>
  </section>

  <section class="section-block section-about">
    <div class="container about-split">
      <div class="about-text reveal-left">
        <span class="section-label">{svc['num']} — Detail</span>
        <h2 data-i18n="{_it_key(slug, 'title')}">{svc['title']}</h2>
        <p data-i18n="{_it_key(slug, 'lead')}">{svc['lead']}</p>
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
        <h2 data-i18n="it.detail.processTitle">ご支援の流れ</h2>
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
        <h2 data-i18n="it.detail.benefitsTitle">導入メリット</h2>
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
        <h2 data-i18n="it.detail.relatedTitle">関連サービス</h2>
        <p data-i18n="it.detail.relatedLead">あわせてご検討いただけるITサービス</p>
      </div>
      <div class="biz-field-grid">
{related}
      </div>
    </div>
  </section>

  <section class="section-block section-cta-banner">
    <div class="container cta-inner reveal">
      <h2 data-i18n="{_it_key(slug, 'ctaTitle')}">{svc['title']}に関するご相談</h2>
      <p data-i18n="it.detail.ctaLead">まずはお気軽にお問い合わせください。課題に合わせたご提案をいたします。</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-white" data-i18n="it.detail.ctaContact">お問い合わせ</a>
        <a href="it-services.html" class="btn btn-outline-white" data-i18n="it.detail.ctaList">サービス一覧へ</a>
      </div>
    </div>
  </section>

</main>"""
        write_fullwidth_page(
            f"{slug}.html",
            svc["title"],
            f"{slug}.html",
            content_html,
        )
def _it_service_i18n_entries(svc: dict) -> tuple[dict, dict]:
    """Build ja/vi dict entries for one IT service."""
    slug = svc["slug"]
    ja, vi = {}, {}
    mapping = [
        ("title", svc["title"], svc["title_vi"]),
        ("summary", svc["summary"], svc["summary_vi"]),
        ("lead", svc["lead"], svc["lead_vi"]),
        ("ctaTitle", f"{svc['title']}に関するご相談", f"Tư vấn về {svc['title_vi']}"),
    ]
    for part, j, v in mapping:
        k = _it_key(slug, part)
        ja[k] = j
        vi[k] = v
    for i, ((jt, jd), (vt, vd)) in enumerate(zip(svc["features"], svc["features_vi"]), start=1):
        ja[_it_key(slug, f"feat{i}Title")] = jt
        ja[_it_key(slug, f"feat{i}Desc")] = jd
        vi[_it_key(slug, f"feat{i}Title")] = vt
        vi[_it_key(slug, f"feat{i}Desc")] = vd
    for i, ((jt, jd), (vt, vd)) in enumerate(zip(svc["process"], svc["process_vi"]), start=1):
        ja[_it_key(slug, f"proc{i}Title")] = jt
        ja[_it_key(slug, f"proc{i}Desc")] = jd
        vi[_it_key(slug, f"proc{i}Title")] = vt
        vi[_it_key(slug, f"proc{i}Desc")] = vd
    for i, (jb, vb) in enumerate(zip(svc["benefits"], svc["benefits_vi"]), start=1):
        ja[_it_key(slug, f"benefit{i}")] = jb
        vi[_it_key(slug, f"benefit{i}")] = vb
    return ja, vi


def write_i18n_dict() -> None:
    """Emit js/i18n-dict.js from i18n_pages + IT_SERVICES."""
    ja, vi = to_lang_dicts()
    for svc in IT_SERVICES:
        j, v = _it_service_i18n_entries(svc)
        ja.update(j)
        vi.update(v)

    def emit_obj(d: dict) -> str:
        lines = ["{"]
        for k in sorted(d.keys()):
            lines.append(f"    {json.dumps(k, ensure_ascii=False)}: {json.dumps(d[k], ensure_ascii=False)},")
        lines.append("  }")
        return "\n".join(lines)

    out = (
        "window.KATAO_I18N_DICT = {\n"
        f"  ja: {emit_obj(ja)},\n"
        f"  vi: {emit_obj(vi)},\n"
        "};\n"
    )
    path = OUT_DIR / "js" / "i18n-dict.js"
    path.write_text(out, encoding="utf-8")
    print(f"  ✓ js/i18n-dict.js ({len(ja)} keys)")



def main() -> None:
    print("Generating kataosogo-site pages...")
    write_i18n_dict()
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
