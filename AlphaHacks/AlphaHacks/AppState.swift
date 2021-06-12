//
//  Postman.swift
//  AlphaHacks
//
//  Created by Arpan Dhatt on 6/12/21.
//

import SwiftUI

struct CompanyStats : Codable {
    var description: String
    var rating: Float
    var articles: [Article]
}

struct Article : Codable {
    var article_title: String
    var description: String
    var link: String
    var image_link: String
}

class AppState : ObservableObject {
    @Published var companies = ["Test Company 1", "Test Company 2", "Test Company 3"]
    @Published var selectedCompany = "Test Company 1"
    @Published var company_details = CompanyStats(
        description: "Test Description",
        rating: 420.69,
        articles: [
            Article(article_title: "Article Title 1", description: "Article Description 1", link: "https://google.com", image_link: "https://lp-cms-production.imgix.net/2021-01/Nasa%201.jpeg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850"),
            Article(article_title: "Article Title 2", description: "Article Description 2", link: "https://apple.com", image_link: "https://lp-cms-production.imgix.net/2021-01/Nasa%201.jpeg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850"),
        ]
    )
}
