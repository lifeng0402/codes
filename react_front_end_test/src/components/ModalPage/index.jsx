import React, { useState } from 'react';
import { Modal } from 'antd';


const ModalPage = (value) => {
      const [open, setOpen] = useState(false);
      return (
            <div>
                  <Modal
                        title="Modal 1000px width"
                        centered
                        open={open}
                        onOk={() => setOpen(false)}
                        onCancel={() => setOpen(false)}
                        width={1000}
                  >
                        <p>some contents...</p>
                        <p>some contents...</p>
                        <p>some contents...</p>
                  </Modal>
            </div>
      );
};
export default ModalPage;