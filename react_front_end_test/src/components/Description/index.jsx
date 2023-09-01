import { Input, Button } from 'antd';
import './index.css'


const Description = () => {
      return (
            <div className='description-div' >
                  <Input placeholder='Description' className='description-input' />
                  <Button ghost>删除</Button>
            </div>
      )
};
export default Description;