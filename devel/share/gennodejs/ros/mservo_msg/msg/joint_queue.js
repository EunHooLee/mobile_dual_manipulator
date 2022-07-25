// Auto-generated. Do not edit!

// (in-package mservo_msg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let joint_data = require('./joint_data.js');

//-----------------------------------------------------------

class joint_queue {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.jointq = null;
    }
    else {
      if (initObj.hasOwnProperty('jointq')) {
        this.jointq = initObj.jointq
      }
      else {
        this.jointq = new Array(2).fill(new joint_data());
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type joint_queue
    // Check that the constant length array field [jointq] has the right length
    if (obj.jointq.length !== 2) {
      throw new Error('Unable to serialize array field jointq - length must be 2')
    }
    // Serialize message field [jointq]
    obj.jointq.forEach((val) => {
      bufferOffset = joint_data.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type joint_queue
    let len;
    let data = new joint_queue(null);
    // Deserialize message field [jointq]
    len = 2;
    data.jointq = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.jointq[i] = joint_data.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    return 28;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mservo_msg/joint_queue';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '975ac8b6c2831749c6d3e61906fa26d9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    joint_data[2] jointq
    
    ================================================================================
    MSG: mservo_msg/joint_data
    int32[7] pos
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new joint_queue(null);
    if (msg.jointq !== undefined) {
      resolved.jointq = new Array(2)
      for (let i = 0; i < resolved.jointq.length; ++i) {
        if (msg.jointq.length > i) {
          resolved.jointq[i] = joint_data.Resolve(msg.jointq[i]);
        }
        else {
          resolved.jointq[i] = new joint_data();
        }
      }
    }
    else {
      resolved.jointq = new Array(2).fill(new joint_data())
    }

    return resolved;
    }
};

module.exports = joint_queue;
