tcinvest_function_config = {
    "BOND_PIO": {
        # PIO
        "title": "pio.m.t",
        "icon": "dat_lenh_trai_phieu",
        "routingUrl": "/wealthtech-pio",
        "roles": ["customer"],
        "type": "appconfig.bond",
        "description": "pio.m.des",
    },
    "BOND_ORDER": {
        # Đặt lệnh trái phiếu
        "title": "appconfig.customer.orderBonds",
        "icon": "dat_lenh_trai_phieu",
        "routingUrl": "/placing-bond",
        "roles": ["customer"],
        "type": "appconfig.bond",
        "description": "menu.bond.placing"
    },
    "BOND_JOURNEY": {
        # Tư vấn trái phiếu
        "title": "appconfig.customer.bond-journey",
        "icon": "iadvisor",
        "routingUrl": "/placing-nbj2",
        "roles": ["customer", "rm", "wp", "rbo"],
        "type": "appconfig.bond",
        "description": "menu.bond.journey"
    },
    "BOND_PROFESSIONAL": {
        # Nhà đầu tư chuyên nghiệp
        "title": "appconfig.customer.professional",
        "icon": "nha_dau_tu_cn",
        "routingUrl": "/professional-investor",
        "roles": ["customer", "rm", "wp", "rbo"],
        "type": "appconfig.bond",
        "description": "menu.bond.pro"
    },
    "BOND_PLACING_ICONNECT": {
        # Thỏa thuận trái phiếu
        "title": "appconfig.customer.agreementBond",
        "icon": "thoa_thuan_trai_phieu",
        "routingUrl": "/placing-iconnect",
        "roles": ["customer"],
        "type": "appconfig.bond",
        "description": "menu.bond.agreement"
    },
    "BOND_RM_ORDER": {
        # Giới thiệu trái phiếu
        "title": "appconfig.rm.introduceBond",
        "icon": "dat_lenh_trai_phieu",
        "routingUrl": "/rm-placing-bond",
        "roles": ["rm", "wp", "rbo"],
        "type": "appconfig.bond",
    },
    "BOND_RM_PLACING_ICONNECT": {
        # Giới thiệu Thỏa thuận TP
        "title": "appconfig.rm.introduceiconnect",
        "icon": "thoa_thuan_trai_phieu",
        "routingUrl": "/rm-placing-iconnect",
        "roles": ["rm", "wp", "rbo"],
        "type": "appconfig.bond",
    },
    "BOND_ICONNECT_BAOLOC": {
        # CD-iconnect
        "title": "appconfig.rm.baoloc",
        "icon": "baoloc",
        "routingUrl": "/iconnect-baoloc",
        "roles": ["rm", "Application/RBO", "rbo"],
        "type": "appconfig.bond",
    },
    "PLEDGING_BOND": {
        "title": "appconfig.rm.pledging",
        "icon": "pledging",
        "routingUrl": "/rm-pledging",
        "roles": ["rm", "rbo"],
        "type": "appconfig.bond",
    },
    "BOND_SALE_SCRIPTS": {
        # Nhận diện nhu cầu KH
        "title": "appconfig.rm.salescripts",
        "icon": "nhandiennhucauKH",
        "routingUrl": "/salescripts",
        "roles": ["rm", "rbo"],
        "viewType": "widget",
        "type": "appconfig.bond",
    },
    "ICONNECT_CONDITION_PLACING": {
        # Đặt lệnh điều kiện iconnect
        "title": "bond.condition.menu.left",
        "icon": "dat_lenh_trai_phieu",
        "routingUrl": "ICONNECT_CONDITION",
        "roles": ["customer"],
        "viewType": "popup",
        "type": "appconfig.bond",
        "description": "menu.bond.iconnect"
    },
    "FUND_ORDER": {
        # Đặt lệnh quỹ
        "title": "appconfig.customer.orderFunds",
        "icon": "dat_lenh_quy",
        "routingUrl": "/placing-fund",
        "roles": ["customer"],
        "type": "appconfig.fund",
        "description": "menu.fund.placing"
    },
    "FUND_TCWEALTH": {
        # Quản lý gia sản
        "title": "appconfig.rm.accumulatedPlan",
        "icon": "ke_hoach_tich_luy",
        "routingUrl": "/tcwealth",
        "roles": ["customer", "rm", "wp"],
        "type": "appconfig.fund",
        "description": "menu.fund.tcwealth"
    },
    "FUND_IPLAN": {
        # Đầu tư tổng hợp
        "title": "appconfig.customer.iplan",
        "icon": "iplan",
        "routingUrl": "/iplan",
        "roles": ["customer"],
        "type": "appconfig.fund",
        "description": "menu.fund.iplan"
    },
    "FUND_CONVERT": {
        # Chuyển đổi quỹ
        "title": "appconfig.customer.tranfersFund",
        "icon": "chuyen_doi_quy",
        "routingUrl": "/fund-convert",
        "roles": ["customer"],
        "type": "appconfig.fund",
        "description": "menu.fund.convert"
    },
    "FUND_RECOMMENDATION": {
        "title": "appconfig.rm.introduceFund",
        "icon": "dat_lenh_quy",
        "routingUrl": "/fund-recommendation",
        "roles": ["rm", "wp", "rbo"],
        "type": "appconfig.fund"
    },
    "FUND_ALLOCATION": {
        # Giới thiệu quỹ
        "title": "fund.balance.assetCode.ALLOCATION",
        "icon": "dat_lenh_quy",
        "routingUrl": "/fund-allocation",
        "roles": ["rm", "wp", "customer"],
        "type": "appconfig.fund"
    },
    "FUND_RM_CONVERT": {
        # Giới thiệu CĐ quỹ
        "title": "appconfig.rm.introduceFundConvert",
        "icon": "chuyen_doi_quy",
        "routingUrl": "/rm-fund-convert",
        "roles": ["rm", "wp"],
        "type": "appconfig.fund"
    },
    "RM_IPLAN": {
        # Đầu tư tổng hợp
        "title": "appconfig.rm.iplan",
        "icon": "iplan",
        "routingUrl": "/rm-iplan",
        "roles": ["rm", "wp"],
        "type": "appconfig.fund"
    },
    "STOCK_ORDER": {
        # Đặt lệnh cổ phiếu
        "title": "appconfig.customer.orderStock",
        "icon": "dat_lenh_co_phieu",
        "routingUrl": "/placing-stock",
        "roles": ["customer"],
        "type": "appconfig.stock",
        "description": "menu.stock.placing"
    },
    "TC_PRICE": {
        # Bảng giá cổ phiếu
        "title": "appconfig.customer.tablePrices",
        "icon": "bang_gia_chung_khoan",
        "routingUrl": "/tc-price",
        "roles": ["customer"],
        "type": "appconfig.stock",
        "description": "menu.stock.tcprice"
    },
    "STOCK_EXTEND_DEBT": {
        # Vay ký quỹ Margin
        "title": "appconfig.customer.renewDebt",
        "icon": "gia_han_no",
        "routingUrl": "/extend-debt",
        "roles": ["customer"],
        "type": "appconfig.stock",
        "description": "menu.stock.margin"
    },
    "TC_ANALYSIS": {
        # Phân tích đầu tư
        "title": "appconfig.customer.stockPortal",
        "icon": "phan_tich_dau_tu",
        "routingUrl": "/tc-price/tc-analysis",
        "roles": ["customer"],
        "type": "appconfig.stock",
        "description": "menu.stock.tca"
    },
    "STOCK_TRANSFER": {
        # Chuyển khoản cổ phiếu
        "title": "appconfig.customer.securitiesTransfer",
        "icon": "chuyen_khoan_chung_khoan",
        "routingUrl": "/transfer-stock",
        "roles": ["customer"],
        "type": "appconfig.stock",
        "description": "menu.stock.transfer"
    },
    "STOCK_PURCHASE_RIGHTS": {
        # Đăng ký quyền mua
        "title": "appconfig.customer.registerBuy",
        "icon": "dang_ky_quyen_mua",
        "routingUrl": "/purchase-rights",
        "roles": ["customer"],
        "type": "appconfig.stock",
        "description": "menu.stock.purchaseRights"
    },
    "STOCK_AGREEMENT": {
        # Thỏa thuận cổ phiếu
        "title": "appconfig.customer.stockAgree",
        "icon": "thoa_thuan_co_phieu",
        "routingUrl": "/agreement-placing-stock",
        "roles": ["customer"],
        "type": "appconfig.stock",
        "description": "menu.stock.agreement"
    },
    "PORTFOLIO_ALLOCATION": {
        # Quản lý danh mục
        "title": "appconfig.portfolio_allocation",
        "icon": "quanlydanhmuc",
        "routingUrl": "/portfolio-allocation",
        "roles": ["customer"],
        "type": "appconfig.stock",
        "description": "menu.stock.porfolio"
    },
    "STOCK_MARKET_SHARE": {
        # Thị trường cổ phiếu
        "title": "appconfig.customer.marketShare",
        "icon": "thi_truong_chung_khoan",
        "routingUrl": "https://www.tcbs.com.vn/marketwatch",
        "roles": ["customer", "rm", "wp", "rbo"],
        "type": "appconfig.stock",
        "isOpenInNewTab": True
    },
    "STOCK_CONDITION_PLACING": {
        # Đặt lệnh điều kiện
        "title": "appconfig.customer.conditionalOrder",
        "icon": "dat_lenh_co_phieu",
        "routingUrl": "MULTI",
        "roles": ["customer"],
        "viewType": "popup",
        "type": "appconfig.stock",
        "description": "menu.stock.condition"
    },
    "STOCK_247_PLACING": {
        # Đặt lệnh 24/7
        "title": "appconfig.customer.247",
        "icon": "dat_lenh_co_phieu",
        "routingUrl": "247",
        "roles": ["customer"],
        "viewType": "popup",
        "type": "appconfig.stock",
    },
    "BACK_TEST": {
        # Kiểm thử danh mục
        "title": "menu.backTest.title",
        "icon": "BACK_TEST",
        "routingUrl": "BACK_TEST",
        "roles": ["customer"],
        "viewType": "popup",
        "type": "appconfig.stock",
        "isUtilityMenu": True,
        "description": "menu.utils.backtest"
    },
    "DYNAMIC_WATCH_LIST": {
        # Bộ lọc thông minh
        "title": "filterWatchList.title",
        "icon": "DYNAMIC_WATCH_LIST",
        "routingUrl": "DYNAMIC_WATCH_LIST",
        "roles": ["customer"],
        "viewType": "popup",
        "type": "appconfig.stock",
        "isUtilityMenu": True,
        "description": "menu.utils.dynamicW"
    },
    "STOCK_MULTIPLE_PLACING": {
        # Lệnh nhóm
        "title": "lookup.stockTransactionHistory.group",
        "icon": "dat_lenh_co_phieu",
        "routingUrl": "/multiple-placing-stock",
        "roles": ["customer"],
        "type": "appconfig.stock",
    },
    "STOCK_EXCEL_PLACING": {
        # Đặt lệnh Excel
        "title": "appconfig.customer.excelPlacingStock",
        "icon": "dat_lenh_co_phieu",
        "routingUrl": "/excel-placing-stock",
        "roles": ["customer"],
        "type": "appconfig.stock",
    },
    "IFENGSHUI": {
        "title": "iFengshui",
        "icon": "iFengshui",
        "routingUrl": "/phong-thuy",
        "roles": ["customer"],
        "type": "appconfig.stock",
        "isUtilityMenu": True,
        "description": "menu.utils.iFengshui"
    },
    "STOCK_I_COPY": {
        # Sao chép đầu tư iCopy
        "title": "appconfig.customer.normal.icopy",
        "icon": "icopy",
        "routingUrl": "/icopy",
        "roles": ["customer"],
        "type": "appconfig.stock",
        "description": "menu.stock.icopy"
    },
    "STOCK_BETA_HEDGING": {
        # Hedging Arbitrage
        "title": "appconfig.customer.hedging",
        "icon": "hedging",
        "routingUrl": "/stock-hedging",
        "roles": ["customer"],
        "type": "appconfig.derivative",
        "description": "menu.dr.hedging"
    },
    "STOCK_SECURITIES_DEPOSITORY": {
        # Securities Depository Arbitrage
        "title": "appconfig.customer.securitiesDepository",
        "icon": "securitiesDepository",
        "routingUrl": "/securities-depository",
        "roles": ["customer"],
        "type": "appconfig.stock",
        "description": "menu.stock.seDepository"
    },
    "DERIVATIVE_PLACING_ORDER": {
        "title": "dr.name",
        "icon": "derivative_placing_order",
        "routingUrl": "/tc-price?table=derivative_vn30",
        "roles": ["customer"],
        "type": "appconfig.derivative",
        "description": "menu.dr.placing"
    },
    "DERIVATIVE_I_COPY": {
        # Sao chép đầu tư iCopy PS
        "title": "appconfig.customer.derivative.icopy",
        "icon": "icopy",
        "routingUrl": "/icopyps",
        "roles": ["customer"],
        "type": "appconfig.derivative",
        "description": "menu.stock.icopy"
    },
    "TOOLBOX_DEPOSIT": {
        "title": "deri.payment",
        "icon": "derivative_deposit",
        "routingUrl": "drDeposit",
        "roles": ["customer"],
        "type": "appconfig.derivative",
        "options": {
            "closeLeftMenu": True
        },
        "place": "toolbox",  # Handle open in toolbox,
        "description": "menu.dr.deposit"
    },
    "DR_GUIDE": {
        "title": "dr.guide",
        "icon": "derivative_guide",
        "routingUrl": "drGuide",
        "roles": ["customer"],
        "type": "appconfig.derivative",
        "description": "menu.dr.guide",
        "isOpenInNewTab": True,
    },
    "DERIVATIVE_PLACING_ORDER_PERFORMANCE": {
        "title": "dr.order_performance",
        "icon": "placing_performance",
        "routingUrl": "/investment-efficiency-future",
        "roles": ["customer"],
        "type": "appconfig.derivative",
        "description": "menu.dr.placing.performance",
        "isOpenInNewTab": False,
    },
    "ORDER_BOOK": {
        # Sổ lệnh
        "title": "appconfig.customer.Orders",
        "icon": "so_lenh",
        "routingUrl": "/order-book",
        "roles": ["customer"],
        "type": "appconfig.other",
        "description": "menu.other.orderbook"
    },
    "LOOKUP": {
        # Tra cứu lịch sử
        "title": "appconfig.customer.research",
        "icon": "tracuu-home",
        "routingUrl": "/lookup",
        "roles": ["customer"],
        "type": "appconfig.other",
        "description": "menu.other.lookup"
    },
    "ADVANCE_MONEY": {
        # Ứng trước tiền bán
        "title": "appconfig.customer.cashSale",
        "icon": "ung_tien",
        "routingUrl": "/advance-money",
        "roles": ["customer"],
        "type": "appconfig.money",
        "description": "menu.money.debt"
    },
    "TRANSFER_MONEY": {
        # Chuyển tiền
        "title": "appconfig.customer.transfers",
        "icon": "chuyen_tien",
        "routingUrl": "/transfer-money",
        "roles": ["customer"],
        "type": "appconfig.money",
        "description": "menu.money.transfer"
    },
    "ICASH": {
        # iCAP
        "title": "iCAP",
        "icon": "icash",
        "routingUrl": "/cctg",
        "roles": ["customer"],
        "type": "appconfig.money",
        "description": "menu.money.icash"
    },
    "MY_ASSET": {
        # Tài sản của tôi
        "title": "appconfig.customer.myAsset",
        "icon": "tai_san",
        "routingUrl": "/my-asset",
        "roles": ["customer"],
        "type": "appconfig.other",
        "description": "menu.other.assets"
    },
    "PROFILES": {
        # Thiết lập tài khoản
        "title": "appconfig.customer.setupAccount",
        "icon": "profile",
        "routingUrl": "/profiles",
        "roles": ["customer", "rm", "wp"],
        "type": "appconfig.other",
        "description": "menu.other.profiles"
    },
    "MICRO_INVESTING": {
        # Tích luỹ tiền lẻ
        "title": "appconfig.microInvesting",
        "icon": "ic-tichluytienle",
        "routingUrl": "/micro-investing",
        "roles": ["customer"],
        "type": "appconfig.other",
        "isUtilityMenu": True,
        "description": "menu.utils.microSaving"
    },
    "IWEALTH_CLUB": {
        # iWealth Club
        "title": "appconfig.customer.iwealthClub",
        "icon": "iWealthClub",
        "routingUrl": "https://iwealthclub-sit.tcbs.com.vn/user/auth/external?authclient=tcbs",
        "roles": ["customer", "rm", "wp", "rbo"],
        "type": "appconfig.other",
        "isOpenInNewTab": True,
        "description": "menu.other.iWealthClub"
    },
    "RM_ICALENDAR": {
        "title": "appconfig.customer.icalender",
        "icon": "icalendar",
        "routingUrl": "/rm-icalendar",
        "roles": ["rm"],
        "type": "appconfig.other",
        "isUtilityMenu": True
    },
    "RM_LOOKUP": {
        # Tra cứu lịch sử
        "title": "appconfig.rm.researchRM",
        "icon": "tracuu-home",
        "routingUrl": "/rm-lookup",
        "roles": ["rm", "wp", "rbo"],
        "type": "appconfig.other"
    },
    "RM_PERFORMANCE": {
        # Hiệu quả kinh doanh
        "title": "appconfig.myResult",
        "icon": "hieu_qua_dau_tu",
        "routingUrl": "/rm-performance",
        "roles": ["rm"],
        "type": "appconfig.other",
        "isUtilityMenu": True
    },
    "REFERRAL": {
        # Giới thiệu nhận thưởng
        "title": "appconfig.customer.introduceRewards",
        "icon": "gioi_thieu_khach_hang",
        "routingUrl": "/referral",
        "roles": ["customer"],
        "type": "appconfig.other",
        "description": "menu.other.referal"
    },
    "IWEALTH_PARTNER": {
        # Đối tác phát triển KD
        "title": "appconfig.wp.iwealth",
        "icon": "iwealth",
        "routingUrl": "/iwealth-partner",
        "roles": ["wp", "customer"],
        "type": "appconfig.other",
        "description": "menu.other.iWealthPartner"
    },
    "E_VOTING": {
        # Bỏ phiếu điện tử
        "title": "appconfig.customer.e-voting-list",
        "icon": "evoting",
        "routingUrl": "/e-voting-list",
        "roles": ["customer"],
        "type": "appconfig.other",
        "description": "menu.other.evoting"
    },
    "ICALENDAR": {
        "title": "appconfig.customer.icalender",
        "icon": "icalendar",
        "routingUrl": "/icalendar",
        "roles": ["customer"],
        "type": "appconfig.other",
        "isUtilityMenu": True,
        "description": "menu.utils.iCalendar"
    },
    "INVESTMENT_EFFICIENCY": {
        # **Hiệu quả đầu tư * /
        "title": "appconfig.investmentEfficiency",
        "icon": "hieu-qua-dau-tu",
        "routingUrl": "/investment-efficiency",
        "roles": ["customer"],
        "type": "appconfig.other",
        "isUtilityMenu": True,
        "description": "menu.utils.investEff"
    },
    "IXU": {
        "title": "appconfig.ixu",
        "icon": "ixu",
        "routingUrl": "/ixu",
        "roles": ["customer"],
        "type": "appconfig.money",
        "description": "menu.money.ixu"
    },
    "MANUAL": {
        # Hướng dẫn sử dụng
        "title": "appconfig.customer.manual",
        "icon": "huong_dan_su_dung",
        "routingUrl": "https://www.tcbs.com.vn/ho-tro/danh-sach",
        "roles": ["customer", "rm", "wp", "rbo"],
        "type": "appconfig.other",
        "isOpenInNewTab": True
    },
    "RM_CONTACT": {
        "title": "appconfig.rm.contact",
        "icon": "lien_he",
        "routingUrl": "https://www.tcbs.com.vn/ho-tro",
        "roles": ["rm", "wp", "rbo"],
        "type": "appconfig.other",
        "isOpenInNewTab": True
    },
    "TOOLBOX_CANH_BAO": {
        "title": "s_cond.alert-5",
        "icon": "canhbao",
        "routingUrl": "canhbao",
        "roles": ["customer"],
        "type": "toolbar.toolbox",
        "place": "toolbox"  # Handle open in toolbox
    },
    "ISAVE": {
        "title": "isave.placing.text1",
        "icon": "iSAVE",
        "routingUrl": "/isave",
        "roles": ["customer"],
        "type": "appconfig.money",
        "description": "menu.money.isave"
    },
    "BANK_LINK": {
        # Liên kết ngân hàng
        "title": "appconfig.customer.bankLink",
        "icon": "bank_link",
        "routingUrl": "/profiles?c=1",
        "roles": ["customer"],
        "type": "appconfig.other",
        "fullRoutingUrl": True,
        "description": "menu.utils.bank"
    },
    "WATCH_LIST": {
        # Giỏ hàng cho tôi
        "title": "appconfig.customer.wathlist",
        "icon": "watchlist",
        "routingUrl": "/watchlist",
        "roles": ["customer"],
        "type": "appconfig.other",
        "description": "menu.other.watchlist"
    },
    "RM_ICAP": {
        "title": "appconfig.rm.iCAP",
        "icon": "icash",
        "routingUrl": "/rm-cctg",
        "roles": ["rm", "rbo"],
        "type": "appconfig.money",
        "description": "menu.money.icash"
    },
    "RISK_PROFILING": {
        "title": "appconfig.customer.riskProfiling",
        "icon": "riskProfiling",
        "routingUrl": "/risk-profiling",
        "roles": ["customer"],
        "type": "appconfig.other",
        "description": "appconfig.customer.riskProfilingDescription"
    }
}

print("start index tcinvest config by url")
tcinvest_config_indexed_by_url = {}
for feature, data in tcinvest_function_config.items():
    if "viewType" not in data:
        fullUrl = "https://tcinvest.tcbs.com.vn" + data.get("routingUrl")
    else:
        fullUrl = data.get("routingUrl")
    data["feature"] = feature
    tcinvest_config_indexed_by_url[fullUrl] = data

print("tcinvest config indexed done")
