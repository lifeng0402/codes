import React, { useState } from 'react';
import { Input, Checkbox } from 'antd';
import './index.css'


const RequestKey = () => {
      const [isHovered, setIsHovered] = useState(false);
      const [isChecked, setIsChecked] = useState(false);

      const handleMouseEnter = () => {
            setIsHovered(true);
            setIsChecked(true);
      };

      const handleMouseLeave = () => {
            setIsHovered(false);
            setIsChecked(false);
      };

      return (
            <div
                  className='request-key'
                  onMouseEnter={handleMouseEnter}
                  onMouseLeave={handleMouseLeave}
            >
                  {
                        isHovered && <Checkbox
                              className='request-checkbox' checked={isChecked}
                              onChange={e => setIsChecked(e.target.checked)}
                        />
                  }
                  <Input placeholder="Key" />
            </div>
      );
};

export default RequestKey;