(() => {
  const STORAGE_KEY = 'katao_lang';
  const SUPPORTED = ['ja', 'vi'];

  const dict = {
    ja: {
      'loader.text': '読み込み中...',
      'nav.home': 'ホーム',
      'nav.company': '会社概要',
      'nav.greeting': '代表者挨拶',
      'nav.business': '事業内容',
      'nav.it': 'ITサービス',
      'nav.forCompanies': '企業様へ',
      'nav.recruitment': '採用情報',
      'nav.jobs': '求人情報',
      'nav.news': 'ニュース',
      'nav.contact': 'お問い合わせ',
      'nav.menu': 'メニュー',
      'nav.main': 'メインナビゲーション',
      'lang.label': '言語',
      'footer.company': '会社情報',
      'footer.services': 'サービス',
      'footer.contact': 'お問い合わせ',
      'footer.tagline': '機会を繋ぐ・未来を築く',
      'footer.it': 'ITアウトソーシング',
      'footer.offshore': 'オフショア開発',
      'footer.forCompanies': '企業様へ',
      'footer.contactLink': 'お問い合わせ',
      'footer.copy': '© 2026 株式会社カタオ総合 All Rights Reserved.',
      'backToTop': 'トップへ戻る',
      'page.home': 'ホーム | 株式会社カタオ総合',
      'page.jobs': '求人情報 | 株式会社カタオ総合',
      'home.badge': '外国人人材紹介事業',
      'home.heroTitle': '機会を繋ぐ・未来を築く',
      'home.heroLead': 'ベトナムと日本をつなぐ信頼のパートナー — 人材紹介から定着支援までワンストップ',
      'home.ctaCompanies': '企業様はこちら',
      'home.ctaContact': 'お問い合わせ',
      'home.aboutTitle': '日本とベトナムをつなぐ<br>総合人材サービス',
      'home.aboutP1': '株式会社カタオ総合は、革新的なソリューションを提供し、お客様の信頼に応えることを使命としています。ベトナムをはじめとする海外の教育機関・団体との強固なネットワークを活かし、日本語能力・専門スキル・勤労意識に優れた人材を厳選・育成し、日本企業へ紹介しております。',
      'home.aboutP2': '「信頼」「誠実」「挑戦」を企業理念とし、社会に貢献できる企業であり続けます。',
      'home.aboutCta': '会社概要を見る',
      'home.stat1': '設立年',
      'home.stat2': '特定技能業種',
      'home.stat3': '事業分野',
      'home.stat4': 'ワンストップ支援',
      'home.servicesTitle': '事業内容',
      'home.servicesLead': '人材紹介からIT・建設DXまで、事業を幅広く展開',
      'home.jobsBadge': '公開中',
      'home.jobsTitle': '求人サービス',
      'home.jobsDesc': '求職者と企業をつなぐ求人情報サイト。地域・給与での検索、履歴書からの求人提案、応募状況の確認まで。',
      'home.svc1Title': '技能実習・特定技能',
      'home.svc1Desc': '育成・送出し、16業種対応の登録支援機関サービス',
      'home.svc2Title': '高度人材紹介',
      'home.svc2Desc': '技術・人文知識・国際業務ビザ対応',
      'home.svc3Title': '生活・就業支援',
      'home.svc3Desc': 'ビザ、住居、日本語、定着支援のトータルサポート',
      'home.svc4Title': '通訳・翻訳・研修',
      'home.svc4Desc': '言語サービスと教育コンサルティング',
      'home.svc5Title': '日越連携支援',
      'home.svc5Desc': '技術協力・投資・生産分野の国際連携',
      'home.svc6Title': 'ITアウトソーシング',
      'home.svc6Desc': 'オフショア開発、アプリ開発、クラウド、AI、セキュリティなど',
      'home.servicesCta': '事業内容の詳細を見る',
      'home.jobsFind': '求人を探す',
      'home.whyTitle': 'カタオ総合が選ばれる理由',
      'home.why1Title': 'ワンストップ対応',
      'home.why1Desc': '人材選定から採用、入国後の生活・職場定着支援まで一貫したサービス',
      'home.why2Title': 'ベトナム語サポート',
      'home.why2Desc': '面接・生活指導・日常相談すべてベトナム語で対応可能',
      'home.why3Title': '法的手続き代行',
      'home.why3Desc': '在留資格、ビザ発給、入国サポートまで全て代行',
      'home.processTitle': '採用の流れ',
      'home.processLead': '人材募集から就業開始まで5ステップで完全サポート',
      'home.step1Title': '人材募集・紹介',
      'home.step1Desc': 'ご要望をお伺いし最適な人材をご提案',
      'home.step2Title': '面接対応',
      'home.step2Desc': '母国語スタッフが同行サポート',
      'home.step3Title': '内定・書類申請',
      'home.step3Desc': 'ビザ申請などトータルサポート',
      'home.step4Title': '入国準備',
      'home.step4Desc': '生活環境整備を万全に',
      'home.step5Title': '就業開始',
      'home.step5Desc': '定期的フォローアップ',
      'home.ctaTitle': 'まずはお気軽にご相談ください',
      'home.ctaLead': '貴社の人材課題に最適なソリューションをご提案いたします',
      'home.ctaForCompanies': '企業様向け情報',
      'jobs.heroTitle': '求人情報',
      'jobs.heroSub': 'Job Openings',
      'jobs.siteTitle': '求人情報サイト',
      'jobs.siteDesc': '株式会社カタオ総合の求人サービスです。求職者と企業をつなぎ、地域・給与での検索、履歴書からの求人提案、応募状況の確認までを一つのサイトで提供します。特定技能・技術人文知識国際業務など、日本で働く方向けの求人を掲載しています。',
      'jobs.openSite': '求人サイトを開く',
      'jobs.engTitle': '技術・人文知識・国際業務ビザ人材（Engineer / Specialist）',
      'jobs.engDesc': '専門知識と実務経験を活かし、日本企業での中長期的なキャリア形成を目指す方向けの求人カテゴリです。',
      'jobs.sswTitle': '特定技能者（Specified Skilled Worker）',
      'jobs.sswDesc': '特定技能制度の対象分野で、即戦力として活躍したい方向けの求人カテゴリです。',
      'meta.homeDesc': '株式会社カタオ総合 — ベトナムと日本をつなぐ外国人人材紹介・登録支援機関',
    },
    vi: {
      'loader.text': 'Đang tải...',
      'nav.home': 'Trang chủ',
      'nav.company': 'Công ty',
      'nav.greeting': 'Đại diện',
      'nav.business': 'Kinh doanh',
      'nav.it': 'Dịch vụ IT',
      'nav.forCompanies': 'Doanh nghiệp',
      'nav.recruitment': 'Tuyển dụng',
      'nav.jobs': 'Việc làm',
      'nav.news': 'Tin tức',
      'nav.contact': 'Liên hệ',
      'nav.menu': 'Menu',
      'nav.main': 'Điều hướng chính',
      'lang.label': 'Ngôn ngữ',
      'footer.company': 'Thông tin công ty',
      'footer.services': 'Dịch vụ',
      'footer.contact': 'Liên hệ',
      'footer.tagline': 'Kết nối cơ hội · Xây dựng tương lai',
      'footer.it': 'IT Outsourcing',
      'footer.offshore': 'Phát triển offshore',
      'footer.forCompanies': 'Dành cho doanh nghiệp',
      'footer.contactLink': 'Liên hệ',
      'footer.copy': '© 2026 Công ty cổ phần Katao Sogo. Bảo lưu mọi quyền.',
      'backToTop': 'Lên đầu trang',
      'page.home': 'Trang chủ | Công ty cổ phần Katao Sogo',
      'page.jobs': 'Thông tin việc làm | Công ty cổ phần Katao Sogo',
      'home.badge': 'Giới thiệu nhân sự nước ngoài',
      'home.heroTitle': 'Kết nối cơ hội · Xây dựng tương lai',
      'home.heroLead': 'Đối tác tin cậy kết nối Việt Nam và Nhật Bản — từ giới thiệu nhân sự đến hỗ trợ gắn bó',
      'home.ctaCompanies': 'Dành cho doanh nghiệp',
      'home.ctaContact': 'Liên hệ',
      'home.aboutTitle': 'Dịch vụ nhân sự tổng hợp<br>kết nối Nhật Bản và Việt Nam',
      'home.aboutP1': 'Công ty cổ phần Katao Sogo lấy sứ mệnh cung cấp giải pháp sáng tạo và đáp ứng niềm tin của khách hàng. Với mạng lưới vững chắc cùng các cơ sở giáo dục và tổ chức tại Việt Nam cùng các nước khác, chúng tôi tuyển chọn và đào tạo nhân sự có năng lực tiếng Nhật, kỹ năng chuyên môn và ý thức làm việc cao để giới thiệu tới doanh nghiệp Nhật Bản.',
      'home.aboutP2': 'Với tinh thần “Tin cậy · Chính trực · Thách thức”, chúng tôi phấn đấu trở thành doanh nghiệp đóng góp cho xã hội.',
      'home.aboutCta': 'Xem giới thiệu công ty',
      'home.stat1': 'Năm thành lập',
      'home.stat2': 'Ngành kỹ năng đặc định',
      'home.stat3': 'Lĩnh vực kinh doanh',
      'home.stat4': 'Hỗ trợ one-stop',
      'home.servicesTitle': 'Lĩnh vực kinh doanh',
      'home.servicesLead': 'Từ giới thiệu nhân sự đến IT và DX xây dựng — mở rộng đa lĩnh vực',
      'home.jobsBadge': 'Đang mở',
      'home.jobsTitle': 'Dịch vụ việc làm',
      'home.jobsDesc': 'Nền tảng kết nối ứng viên và doanh nghiệp: tìm theo khu vực·mức lương, gợi ý việc từ CV, theo dõi trạng thái ứng tuyển.',
      'home.svc1Title': 'Thực tập kỹ năng · Kỹ năng đặc định',
      'home.svc1Desc': 'Đào tạo·đưa đi làm việc, hỗ trợ đăng ký cho 16 ngành',
      'home.svc2Title': 'Giới thiệu nhân sự cao cấp',
      'home.svc2Desc': 'Visa kỹ thuật·kiến thức nhân văn·nghiệp vụ quốc tế',
      'home.svc3Title': 'Hỗ trợ sinh hoạt·việc làm',
      'home.svc3Desc': 'Visa, chỗ ở, tiếng Nhật, hỗ trợ gắn bó tại nơi làm việc',
      'home.svc4Title': 'Phiên dịch·dịch thuật·đào tạo',
      'home.svc4Desc': 'Dịch vụ ngôn ngữ và tư vấn giáo dục',
      'home.svc5Title': 'Hỗ trợ liên kết Nhật–Việt',
      'home.svc5Desc': 'Hợp tác kỹ thuật·đầu tư·sản xuất quốc tế',
      'home.svc6Title': 'IT Outsourcing',
      'home.svc6Desc': 'Offshore, phát triển ứng dụng, cloud, AI, bảo mật…',
      'home.servicesCta': 'Xem chi tiết lĩnh vực kinh doanh',
      'home.jobsFind': 'Tìm việc làm',
      'home.whyTitle': 'Vì sao chọn Katao Sogo',
      'home.why1Title': 'Hỗ trợ one-stop',
      'home.why1Desc': 'Từ tuyển chọn đến tuyển dụng, hỗ trợ sinh hoạt và gắn bó sau khi nhập cảnh',
      'home.why2Title': 'Hỗ trợ tiếng Việt',
      'home.why2Desc': 'Phỏng vấn, hướng dẫn sinh hoạt, tư vấn hàng ngày bằng tiếng Việt',
      'home.why3Title': 'Đại diện thủ tục pháp lý',
      'home.why3Desc': 'Tư cách lưu trú, cấp visa, hỗ trợ nhập cảnh',
      'home.processTitle': 'Quy trình tuyển dụng',
      'home.processLead': 'Hỗ trợ trọn vẹn 5 bước từ tuyển nhân sự đến bắt đầu làm việc',
      'home.step1Title': 'Tuyển·giới thiệu nhân sự',
      'home.step1Desc': 'Lắng nghe nhu cầu và đề xuất ứng viên phù hợp',
      'home.step2Title': 'Phỏng vấn',
      'home.step2Desc': 'Nhân viên bản ngữ đồng hành hỗ trợ',
      'home.step3Title': 'Nhận việc·nộp hồ sơ',
      'home.step3Desc': 'Hỗ trợ toàn diện gồm xin visa',
      'home.step4Title': 'Chuẩn bị nhập cảnh',
      'home.step4Desc': 'Chuẩn bị môi trường sinh hoạt đầy đủ',
      'home.step5Title': 'Bắt đầu làm việc',
      'home.step5Desc': 'Theo dõi định kỳ sau khi vào việc',
      'home.ctaTitle': 'Hãy liên hệ với chúng tôi',
      'home.ctaLead': 'Chúng tôi đề xuất giải pháp phù hợp với thách thức nhân sự của quý công ty',
      'home.ctaForCompanies': 'Thông tin dành cho doanh nghiệp',
      'jobs.heroTitle': 'Thông tin việc làm',
      'jobs.heroSub': 'Job Openings',
      'jobs.siteTitle': 'Trang việc làm',
      'jobs.siteDesc': 'Dịch vụ việc làm của Công ty cổ phần Katao Sogo. Kết nối ứng viên và doanh nghiệp trong một nền tảng: tìm theo khu vực·mức lương, gợi ý việc từ CV, theo dõi ứng tuyển. Đăng tin dành cho người làm việc tại Nhật (kỹ năng đặc định, kỹ thuật·nhân văn·nghiệp vụ quốc tế…).',
      'jobs.openSite': 'Mở trang việc làm',
      'jobs.engTitle': 'Nhân sự visa kỹ thuật·nhân văn·nghiệp vụ quốc tế (Engineer / Specialist)',
      'jobs.engDesc': 'Danh mục việc làm dành cho người muốn phát triển sự nghiệp trung–dài hạn tại doanh nghiệp Nhật bằng chuyên môn và kinh nghiệm thực tế.',
      'jobs.sswTitle': 'Người lao động kỹ năng đặc định (Specified Skilled Worker)',
      'jobs.sswDesc': 'Danh mục việc làm cho các lĩnh vực thuộc chế độ kỹ năng đặc định, dành cho người muốn làm việc ngay với năng lực sẵn có.',
      'meta.homeDesc': 'Công ty cổ phần Katao Sogo — giới thiệu nhân sự nước ngoài và cơ quan hỗ trợ đăng ký kết nối Việt Nam–Nhật Bản',
    },
  };

  function currentLang() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (SUPPORTED.includes(saved)) return saved;
    return 'ja';
  }

  function t(lang, key) {
    return (dict[lang] && dict[lang][key]) || (dict.ja && dict.ja[key]) || key;
  }

  function apply(lang) {
    if (!SUPPORTED.includes(lang)) lang = 'ja';
    localStorage.setItem(STORAGE_KEY, lang);
    document.documentElement.lang = lang === 'vi' ? 'vi' : 'ja';
    document.body.classList.remove('lang-ja', 'lang-vi');
    document.body.classList.add(lang === 'vi' ? 'lang-vi' : 'lang-ja');

    const extra = window.KATAO_I18N_DICT || {};
    const pack = Object.assign({}, dict[lang] || {}, extra[lang] || {});
    const fallback = Object.assign({}, dict.ja || {}, extra.ja || {});

    const translate = (key) => pack[key] || fallback[key] || key;

    document.querySelectorAll('[data-i18n]').forEach((el) => {
      const key = el.getAttribute('data-i18n');
      if (!key) return;
      el.textContent = translate(key);
    });

    document.querySelectorAll('[data-i18n-html]').forEach((el) => {
      const key = el.getAttribute('data-i18n-html');
      if (!key) return;
      el.innerHTML = translate(key);
    });

    document.querySelectorAll('[data-i18n-aria]').forEach((el) => {
      const key = el.getAttribute('data-i18n-aria');
      if (!key) return;
      el.setAttribute('aria-label', translate(key));
    });

    const pageKey = document.documentElement.getAttribute('data-page-title');
    if (pageKey) {
      document.title = translate(pageKey);
    }

    const meta = document.querySelector('meta[name="description"][data-i18n-content]');
    if (meta) {
      meta.setAttribute('content', translate(meta.getAttribute('data-i18n-content')));
    }

    document.querySelectorAll('.lang-btn').forEach((btn) => {
      const active = btn.getAttribute('data-lang') === lang;
      btn.classList.toggle('is-active', active);
      btn.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
  }

  function init() {
    apply(currentLang());
    document.querySelectorAll('.lang-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        apply(btn.getAttribute('data-lang') || 'ja');
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.KataoI18n = { apply, currentLang, t };
})();
