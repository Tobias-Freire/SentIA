package com.sentia.notification_service.service;

import com.sentia.notification_service.entity.EmailDetails;
import com.sentia.notification_service.model.FeedbackModel;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EmailTemplateService {

    public EmailDetails createDailyNotificationEmail(String recipient, long negDailyCount, List<FeedbackModel> feedbacks) {
        String subject = "Daily SentIA Notification Service";
        String body = String.format("""
                Hi!
                
                SentIA team wants to inform you that the maximum negative feedbacks limit for the day has been reached.
                
                We detected %d negative feedbacks in the last analysis. It is suggested for you to
                go to your dashboard and check it.

                Wish you all the best,
                SentIA team.
                """, negDailyCount);

        EmailDetails emailDetails = new EmailDetails();

        emailDetails.setRecipient(recipient);
        emailDetails.setSubject(subject);
        emailDetails.setBody(body);

        return emailDetails;
    }

    public EmailDetails createWeeklyNotificationEmail(String recipient, long negWeeklyCount, List<FeedbackModel> feedbacks) {
        String subject = "Weekly SentIA Notification Service";
        String body = String.format("""
                Hi!
                
                SentIA team wants to inform you that the maximum negative feedbacks limit for the week has been reached.
                
                We detected %d negative feedbacks in the last analysis. It is suggested for you to
                go to your dashboard and check it.
                
                Wish you all the best,
                SentIA team.
                """, negWeeklyCount);

        EmailDetails emailDetails = new EmailDetails();

        emailDetails.setRecipient(recipient);
        emailDetails.setSubject(subject);
        emailDetails.setBody(body);

        return emailDetails;
    }
}
