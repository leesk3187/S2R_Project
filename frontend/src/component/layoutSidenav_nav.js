import { Link, NavLink } from 'react-router-dom';

export default function Sidenav() {
    return (
        <div id="layoutSidenav_nav">
            <nav className="sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
                <div className="sb-sidenav-menu">
                    <div className="nav">
                        <div className="sb-sidenav-menu-heading">Main</div>
                        <NavLink className="nav-link" to="/">
                            <div className="sb-nav-link-icon"><i className="fas fa-tachometer-alt"></i></div>
                            Main Page
                        </NavLink>
                        <div className="sb-sidenav-menu-heading">Interface</div>
                        {/* 다음 링크들은 접히는 메뉴를 위한 링크이기 때문에 복잡한 구조를 가지고 있습니다. */}
                        {/* 여기서는 Bootstrap의 collapse 기능과 react-router-dom을 함께 사용하고 있습니다. */}
                        <NavLink className="nav-link collapsed" to="#collapseLayouts" data-bs-toggle="collapse" aria-expanded="false" aria-controls="collapseLayouts">
                            <div className="sb-nav-link-icon"><i className="fas fa-columns"></i></div>
                            Success IP
                            <div className="sb-sidenav-collapse-arrow"><i className="fas fa-angle-down"></i></div>
                        </NavLink>
                        {/* 이하 collapse 구조는 실제로 React에서 동적으로 처리해야 할 수도 있으니 참고용으로만 봐주세요. */}
                        {/* 실제로는 state를 사용하여 접히는 메뉴의 상태를 관리하고, NavLink의 to 속성에는 실제 경로를 제공해야 합니다. */}
                        {/* ... 나머지 코드는 생략 ... */}
                    </div>
                </div>
                <div className="sb-sidenav-footer">
                    <div className="small">Logged in as:</div>
                    IP Information
                </div>
            </nav>
        </div>
    );
}
