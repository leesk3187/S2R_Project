import React from 'react';

function MapIPPage() {
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

export default MapIPPage;
