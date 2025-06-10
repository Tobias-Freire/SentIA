package com.sentia.notification_service.service;

import com.sentia.notification_service.entity.EmailDetails;
import com.sentia.notification_service.model.FeedbackModel;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EmailTemplateService {

    public EmailDetails createEmail(String recipient, long negCount, List<FeedbackModel> feedbacks) {
        String subject = "SentIA Notification Service";
        String body = String.format("""
                Hi!
                
                SentIA team wants to inform you that the maximum negative feedbacks limit has been reached.
                
                We detected %d negative feedbacks in the last analysis. It is suggested for you to
                go to your dashboard and check it.
                
                First negative feedback: %s
                
                Wish you all the best,
                SentIA team.
                """, negCount, feedbacks.getFirst().getFeedback());

        EmailDetails emailDetails = new EmailDetails();

        emailDetails.setRecipient(recipient);
        emailDetails.setSubject(subject);
        emailDetails.setBody(body);

        return emailDetails;
    }
}
