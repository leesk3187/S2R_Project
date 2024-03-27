import React from 'react';

function FailIPPage() {
  return (
    <div>
       <Title />
       <div id='layoutSidenav'>
            <Sidenav />
            <div>
                <main>
                    <Content />
                    <Row />
                    <DataTable data={data}  />
              </main>  
            </div>
        </div>
    </div>
  );
}

export default FailIPPage;
