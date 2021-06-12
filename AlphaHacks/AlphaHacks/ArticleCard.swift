//
//  ArticleCard.swift
//  AlphaHacks
//
//  Created by Arpan Dhatt on 6/12/21.
//

import SwiftUI

struct ArticleCard: View {
    var article: Article
    
    var body: some View {
        HStack {
            ImageView(withURL: article.image_link).cornerRadius(10.0)
            VStack(alignment: .leading) {
                Text(article.article_title).font(.title2)
                Text(article.description).font(.caption)
            }
        }.frame(height: 100).onTapGesture {
            UIApplication.shared.open(URL(string: article.link)!)
        }
    }
}

struct ArticleCard_Previews: PreviewProvider {
    static var previews: some View {
        ArticleCard(article: Article(article_title: "Article Title 1", description: "Article Description 1 Article Description 1 Article Description 1 Article Description 1 Article Description 1 ", link: "https://google.com", image_link: "https://lp-cms-production.imgix.net/2021-01/Nasa%201.jpeg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850"))
    }
}
