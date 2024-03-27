import { Link } from 'react-router-dom';

export default function Title() {
    return (
        <nav className="sb-topnav navbar navbar-expand navbar-dark bg-dark">
            {/* React Router의 Link 컴포넌트를 사용 */}
            <Link className="navbar-brand ps-3" to="/">IP Information</Link>
            <button className="btn btn-link btn-sm order-1 order-lg-0 me-4 me-lg-0" id="sidebarToggle"><i className="fas fa-bars"></i></button>
        </nav>
    );
}