package com.sentia.notification_service.service;

import com.sentia.notification_service.entity.EmailDetails;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
public class EmailService {

    @Autowired
    private JavaMailSender javaMailSender;

    @Value("${sender_email}")
    private String sender_email;

    public String sendEmail(EmailDetails emailDetails) {
        try {
            SimpleMailMessage message = new SimpleMailMessage();

            message.setFrom(sender_email);
            message.setTo(emailDetails.getRecipient());
            message.setSubject(emailDetails.getSubject());
            message.setText(emailDetails.getBody());

            javaMailSender.send(message);
            return "Email sent successfully!";
        } catch (Exception e) {
            return "Error sending email!" + e.getMessage();
        }
    }
}
