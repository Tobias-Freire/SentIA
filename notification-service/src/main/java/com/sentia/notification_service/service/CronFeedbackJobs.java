package com.sentia.notification_service.service;

import com.sentia.notification_service.entity.EmailDetails;
import com.sentia.notification_service.model.FeedbackModel;
import com.sentia.notification_service.repository.FeedbackRepository;
import org.springframework.beans.factory.annotation.Value;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Slf4j
@Service
public class CronFeedbackJobs {

    private final FeedbackRepository feedbackRepository;
    private final EmailService emailService;

    public CronFeedbackJobs(FeedbackRepository feedbackRepository, EmailService emailService) {
        this.feedbackRepository = feedbackRepository;
        this.emailService = emailService;
    }

    @Value("${count_to_trigger}")
    private int count_to_trigger;

    @Value("${receiver_email}")
    private String receiver_email;

    @Scheduled(cron = "00 58 10 * * *")
    public void processDailyNegativeFeedbacks() {
        LocalDateTime end = LocalDateTime.now();
        LocalDateTime start = end.minusDays(1);

        List<FeedbackModel> feedbacks = feedbackRepository.findAllNegativeClassificationsByDateRange(start, end);
        long count = feedbackRepository.countNegativeClassificationsByDateRange(start, end);

        if (count >= count_to_trigger) {
            EmailTemplateService emailTemplateService = new EmailTemplateService();
            EmailDetails emailDetails = emailTemplateService.createEmail(receiver_email, count, feedbacks);

            emailService.sendEmail(emailDetails);
        }
    }
}
