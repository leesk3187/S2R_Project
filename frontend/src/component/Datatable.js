import '../css/DataTable.css'
// import '../index.css'

export default function DataTable({data}) {
    return(
      <table className="table">
      <thead>
        <tr>
          <th>최초접속일</th>
          <th>접속유형</th>
          <th>IP</th>
          <th>국가</th>
          <th>상태</th>
          <th>상세보기</th>
        </tr>
      </thead>
      <tbody>
        {data.map((row, index) => (
          <tr key={index}>
            <td>{row.firstAccessDate}</td>
            <td>{row.accessType}</td>
            <td>{row.ip}</td>
            <td>{row.country}</td>
            <td>{row.status}</td>
            <td>
              {/* 더보기 버튼 또는 링크 구현 */}
              <button onClick={() => handleMoreClick(row)}>더보기</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
  }

  // 더보기 버튼 클릭 이벤트 핸들러
const handleMoreClick = (rowData) => {
  // 여기에 더보기를 클릭했을 때 수행할 로직을 구현합니다.
  console.log('더보기 클릭', rowData);
};