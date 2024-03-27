import { Link } from 'react-router-dom';

export default function Row() {
    return (
        <div className="row">
            <div className="col-xl-3 col-md-6">
                <div className="card bg-primary text-white mb-4">
                    <div className="card-body">IP List</div>
                    <div className="card-footer d-flex align-items-center justify-content-between">
                        <Link className="small text-white stretched-link" to="/">View Details</Link>
                        <div className="small text-white"><i className="fas fa-angle-right"></i></div>
                    </div>
                </div>
            </div>
            {/* 다른 카드 항목도 동일한 방식으로 수정 */}
            <div className="col-xl-3 col-md-6">
                <div className="card bg-warning text-white mb-4">
                    <div className="card-body">Map</div>
                    <div className="card-footer d-flex align-items-center justify-content-between">
                        <Link className="small text-white stretched-link" to="/map">View Details</Link>
                        <div className="small text-white"><i className="fas fa-angle-right"></i></div>
                    </div>
                </div>
            </div>
            <div className="col-xl-3 col-md-6">
                <div className="card bg-success text-white mb-4">
                    <div className="card-body">Success IP</div>
                    <div className="card-footer d-flex align-items-center justify-content-between">
                        <Link className="small text-white stretched-link" to="/success-ip">View Details</Link>
                        <div className="small text-white"><i className="fas fa-angle-right"></i></div>
                    </div>
                </div>
            </div>
            <div className="col-xl-3 col-md-6">
                <div className="card bg-danger text-white mb-4">
                    <div className="card-body">Failed IP</div>
                    <div className="card-footer d-flex align-items-center justify-content-between">
                        <Link className="small text-white stretched-link" to="/failed-ip">View Details</Link>
                        <div className="small text-white"><i className="fas fa-angle-right"></i></div>
                    </div>
                </div>
            </div>
        </div>
    );
}
