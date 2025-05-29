package com.sentia.notification_service.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
public class EmailService {

    @Autowired
    private JavaMailSender mailSender;

    @Value("${spring.mail.username}")
    private String sender_email;

    public void sendEmail(String receiver, String subject, String body) {
        SimpleMailMessage message = new SimpleMailMessage();
        message.setFrom(sender_email);
        message.setTo(receiver);
        message.setSubject(subject);
        message.setText(body);

        mailSender.send(message);
    }
}
