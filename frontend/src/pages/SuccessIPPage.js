import React from 'react';

function SuccessIPPage() {
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

export default SuccessIPPage;
