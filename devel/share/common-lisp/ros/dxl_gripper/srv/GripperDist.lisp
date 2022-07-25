; Auto-generated. Do not edit!


(cl:in-package dxl_gripper-srv)


;//! \htmlinclude GripperDist-request.msg.html

(cl:defclass <GripperDist-request> (roslisp-msg-protocol:ros-message)
  ((dist
    :reader dist
    :initarg :dist
    :type cl:float
    :initform 0.0))
)

(cl:defclass GripperDist-request (<GripperDist-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GripperDist-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GripperDist-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dxl_gripper-srv:<GripperDist-request> is deprecated: use dxl_gripper-srv:GripperDist-request instead.")))

(cl:ensure-generic-function 'dist-val :lambda-list '(m))
(cl:defmethod dist-val ((m <GripperDist-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dxl_gripper-srv:dist-val is deprecated.  Use dxl_gripper-srv:dist instead.")
  (dist m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GripperDist-request>) ostream)
  "Serializes a message object of type '<GripperDist-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dist))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GripperDist-request>) istream)
  "Deserializes a message object of type '<GripperDist-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dist) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GripperDist-request>)))
  "Returns string type for a service object of type '<GripperDist-request>"
  "dxl_gripper/GripperDistRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GripperDist-request)))
  "Returns string type for a service object of type 'GripperDist-request"
  "dxl_gripper/GripperDistRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GripperDist-request>)))
  "Returns md5sum for a message object of type '<GripperDist-request>"
  "47ad84b25c08b18a1fb3684555468caf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GripperDist-request)))
  "Returns md5sum for a message object of type 'GripperDist-request"
  "47ad84b25c08b18a1fb3684555468caf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GripperDist-request>)))
  "Returns full string definition for message of type '<GripperDist-request>"
  (cl:format cl:nil "float32 dist~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GripperDist-request)))
  "Returns full string definition for message of type 'GripperDist-request"
  (cl:format cl:nil "float32 dist~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GripperDist-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GripperDist-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GripperDist-request
    (cl:cons ':dist (dist msg))
))
;//! \htmlinclude GripperDist-response.msg.html

(cl:defclass <GripperDist-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass GripperDist-response (<GripperDist-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GripperDist-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GripperDist-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dxl_gripper-srv:<GripperDist-response> is deprecated: use dxl_gripper-srv:GripperDist-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <GripperDist-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dxl_gripper-srv:result-val is deprecated.  Use dxl_gripper-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GripperDist-response>) ostream)
  "Serializes a message object of type '<GripperDist-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GripperDist-response>) istream)
  "Deserializes a message object of type '<GripperDist-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GripperDist-response>)))
  "Returns string type for a service object of type '<GripperDist-response>"
  "dxl_gripper/GripperDistResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GripperDist-response)))
  "Returns string type for a service object of type 'GripperDist-response"
  "dxl_gripper/GripperDistResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GripperDist-response>)))
  "Returns md5sum for a message object of type '<GripperDist-response>"
  "47ad84b25c08b18a1fb3684555468caf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GripperDist-response)))
  "Returns md5sum for a message object of type 'GripperDist-response"
  "47ad84b25c08b18a1fb3684555468caf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GripperDist-response>)))
  "Returns full string definition for message of type '<GripperDist-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GripperDist-response)))
  "Returns full string definition for message of type 'GripperDist-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GripperDist-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GripperDist-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GripperDist-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GripperDist)))
  'GripperDist-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GripperDist)))
  'GripperDist-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GripperDist)))
  "Returns string type for a service object of type '<GripperDist>"
  "dxl_gripper/GripperDist")